from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class project (models.Model):
    name = models.CharField(max_length=200)
    start_date= models.DateField()
    responisble= models.ForeignKey(User, on_delete=models.CASCADE)
    week_number= models. CharField (max_length=2, blank=True) 
    end_date= models.DateField() 

    def _str_(self):
        return str(self.name)
    def save(self, *args, **kwargs): 
        print(self.start_date.isocalendar())
        super().save(*args, **kwargs)
