from django.db import models

# Create your models here.

class UserType(models.Model):
    userType = models.CharField(max_length=20)
    def __str__(self):
        return self.userType
    
class User(models.Model):
    userType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    def __str__(self):
            return self.username

    
