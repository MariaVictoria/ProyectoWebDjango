from django.db import models

# Create your models here.

class Programmer (models.Model):
    fullname = models.CharField(max_length=100) 
    nickyname = models.CharField(max_length=50)
    age= models.PositiveSmallIntegerField()
    is_activated=models.BooleanField(default=True)
    
    
    
    

