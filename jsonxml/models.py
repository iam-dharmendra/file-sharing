from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(default='',max_length=15)
    emai=models.EmailField(default='',max_length=15)
    age=models.IntegerField()
    DOB=models.DateField()


    def __str__(self) -> str:
        return self.name