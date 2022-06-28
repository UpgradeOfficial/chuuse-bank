from django.db import models
from django.contrib.auth.models import AbstractUser
from core.utils import random_with_N_digits
from core.models import CoreModel
# Create your models here.


class User(AbstractUser, CoreModel):
    account_number = models.PositiveIntegerField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.account_number = random_with_N_digits(10)
        super().save(*args, **kwargs) 
