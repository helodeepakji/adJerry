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
    
class Sign_up(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Cpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.FirstName
    
    