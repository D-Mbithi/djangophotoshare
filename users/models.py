from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".title()
        
        return full_name
