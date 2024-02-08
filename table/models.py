from django.db import models

# Create your models here.
class storedata(models.Model):
    first=models.CharField(max_length=250)
    second=models.CharField(max_length=250)
    result=models.CharField(max_length=250,null=True)

