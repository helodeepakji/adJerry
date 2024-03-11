from django.db import models

# Create your models here.
class Contact(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Subject=models.CharField(max_length=50)
    Message=models.TextField()
    
    def __str__(self):
        return self.FirstName