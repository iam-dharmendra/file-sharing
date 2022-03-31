from django.db import models

# Create your models here.


class postgreydb(models.Model):
    
    name=models.CharField(default='',max_length=25)
    email=models.EmailField(default='',max_length=25)
    age=models.IntegerField()

    def __str__(self) -> str:
        return self.name