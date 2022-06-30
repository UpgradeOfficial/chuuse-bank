from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import CoreModel
from django.db.models import Sum

from core.utils import random_with_N_digits

# Create your models here.


class User(AbstractUser, CoreModel):
    account_number = models.PositiveIntegerField(unique=True, null=True, blank=True)

    @property
    def balance(self, *args, **kwargs):
        total_deposit = self.transaction_set.filter(account=self, transaction_type="DEPOSIT").aggregate(sum=Sum('amount'))['sum'] or 0
        total_withdrawal = self.transaction_set.filter(account=self, 
        transaction_type="WITHDRAWAL").aggregate(sum=Sum('amount'))['sum'] or 0
        total_balance = total_deposit - total_withdrawal
        return total_balance
    
    def save(self, *args, **kwargs):
        if not self.account_number:
            account_number = None
            while account_number is None:
                account_number = random_with_N_digits(10)
                if User.objects.filter(account_number=account_number).exists():
                    account_number=None
            self.account_number = account_number

        super().save(*args, **kwargs) 
