from email.policy import default
from django.db import models

# Create your models here.

class my_company(models.Model):
    comp=models.CharField(default='',max_length=1000)    
    created_by=models.CharField(default='',max_length=1000)

    def __str__(self) -> str:
        return self.comp



class my_ledger(models.Model):
    company_name=models.ForeignKey(my_company,on_delete=models.CASCADE)
    ledger_list=models.CharField(default='',max_length=1000)
    lcreated_by=models.CharField(default='',max_length=1000)

    def __str__(self) -> str:
        return self.ledger_list


class lUser(models.Model):

    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField()
    password = models.CharField(default='', max_length=15)
    
    def __str__(self):
        return self.name        

class Comments(models.Model):
    user = models.ForeignKey(lUser,on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
