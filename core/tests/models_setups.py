from datetime import date
from time import time
from core.utils import random_with_N_digits
from transaction.models import Transaction
from user.models import User
from django.utils import timezone
from rest_framework.authtoken.models import Token

# Create your tests here.

def create_test_user(username=None, password=None, user_type=None, nop=10):
    random=random_with_N_digits(nop)
    if not password:
        password = random
    if not username:
        username = f"username{random}@gmail.com"
    user = User.objects.create_user(username=username, password=str(password))
    Token.objects.get_or_create(user=user)
    return user

def create_test_transaction(account=None, transaction_type=None, amount=None, created_at=None):

    if not account:
        account = create_test_user()
    if not transaction_type:
        transaction_type = Transaction.TRANSACTION_TYPE.DEPOSIT
    if not amount:
        amount = 1000
    if not created_at:
        created_at=created_at
    return Transaction.objects.create(transaction_type=transaction_type, account=account, amount =amount)

