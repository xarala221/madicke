from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.





class Superviser(models.Model):
    equipement = models.ImageField(upload_to="equipement", null=True, blank=True)
    types = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    
    
    def __str__(self):
       
        return 'configuration'+' '+self.types



