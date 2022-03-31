from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from .utils import *
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    code=models.CharField(blank=True,max_length=15)
    recomend_by=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='ref_by')
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    link=models.CharField(max_length=55,default='')
    t1=models.CharField(default='',max_length=15)

    def __str__(self) -> str:
             
        return f'{self.user.username}-{self.t1}'
   

    def get_recommend_profiles(self):
        qs=Profile.objects.all()
        # my_recs = [p for p in qs if p.recomend_by==self.user]
        my_recs=[]
        for profile in qs:
            if profile.recomend_by==self.user:
                my_recs.append(profile)
        return my_recs        



    def save(self,*args,**kwargs):
        if self.code=='':
            code=genrated_ref_code()
            self.code=code
            self.link="http://127.0.0.1:8000/"+str(self.code)
        super().save(*args,**kwargs)