
from django.db import models

# Create your models here.

class UserDetails(models.Model):

    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField()
    password = models.CharField(default='', max_length=15)
    file= models.FileField(upload_to ='media/',blank=True,null=True,max_length=100)
    received_From = models.CharField(max_length=30, default='',blank=True)
    recieved_file = models.FileField(upload_to='media/', null=False,blank=True)
   

    
    def __str__(self):
        return self.name