from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bio = models.TextField()
    contacts = models.TextField()
    
