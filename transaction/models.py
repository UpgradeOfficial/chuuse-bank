from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from core.models import CoreModel
# Create your models here.
class Transaction(CoreModel):
    
    class TRANSACTION_TYPE(models.TextChoices):
        WITHDRAWAL = "WITHDRAWAL", _("WITHDRAWAL")
        DEPOSIT = "DEPOSIT", _("DEPOSIT")
    account = models.ForeignKey(User, on_delete=models.CASCADE) 
    transaction_type = models.CharField( _("TRANSACTION TYPE"),
        max_length=20,
        choices=TRANSACTION_TYPE.choices,
        default=TRANSACTION_TYPE.DEPOSIT,
    )
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.transaction_type}-{self.amount}-{self.created_at}"

