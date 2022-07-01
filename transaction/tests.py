from datetime import timedelta
from unittest import mock
from django.test import TestCase
from django.urls import reverse
from core.tests.models_setups import create_test_transaction, create_test_user
from transaction.models import Transaction
from django.utils import timezone

from user.models import User

# Create your tests here.

class TestTansaction(TestCase):

 # 1 user
    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_withdrawal(self,  authenticate_function):
        account = create_test_user(password="password")
        deposit = create_test_transaction(account=account)

        authenticate_function.return_value = account, None
        url = reverse("transaction:withdrawal")
        data= {
            "accountNumber":account.account_number, 
            "accountPassword":"password",  
            'withdrawnAmount':1000
        }
        response = self.client.post(url, data=data)
        response_dict = response.json()
        transaction = Transaction.objects.filter(transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL).first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Transaction.objects.count(),2)
        self.assertEqual(response_dict.get('responseCode'),200)
        self.assertEqual(response_dict.get('successful'),True)
        self.assertEqual(response_dict.get('message'),'Your withdrwal of 1000.00 was successfull')
        self.assertEqual(transaction.transaction_type, Transaction.TRANSACTION_TYPE.WITHDRAWAL)

    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_withdrawal_with_wrong_balance(self,  authenticate_function):
        account = create_test_user(password="password")
        deposit  = create_test_transaction(account=account, amount=10)
        authenticate_function.return_value = account, None
        url = reverse("transaction:withdrawal")
        data= {"accountNumber":account.account_number,  "accountPassword":"password",  
            'withdrawnAmount':1000}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Transaction.objects.count(),1)
        self.assertEqual(response_dict.get("non_field_errors")[0],"Your account balance is not enough to withdrawn this sum, balance is 10")

       
    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_withdrawal_with_wrong_user(self,  authenticate_function):
        account = create_test_user()
        account1 = create_test_user()
        authenticate_function.return_value = account, None
        url = reverse("transaction:withdrawal")
        data= {"accountNumber":account1.account_number,  "accountPassword":"password",  
            'withdrawnAmount':1000}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Transaction.objects.count(),0)
        self.assertEqual(response_dict.get("non_field_errors")[0],"Either account doesn't exist or you are not the owner of this account")

    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_deposit(self,  authenticate_function):
        account = create_test_user()
        authenticate_function.return_value = account, None
        url = reverse("transaction:deposit")
        data= {"accountNumber":account.account_number,  'amount':1000}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        transaction = Transaction.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Transaction.objects.count(),1)
        self.assertEqual(transaction.transaction_type, Transaction.TRANSACTION_TYPE.DEPOSIT)
        self.assertEqual(response_dict.get('responseCode'),200)
        self.assertEqual(response_dict.get('successful'),True)
        self.assertEqual(response_dict.get('message'),'Your Deposit of 1000.00 was successfull')

    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_deposit_with_negative_amount(self,  authenticate_function):
        account = create_test_user()
        authenticate_function.return_value = account, None
        url = reverse("transaction:deposit")
        data= {"accountNumber":account.account_number,  'amount':-1000}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        transaction = Transaction.objects.first()
        self.assertEqual(response.status_code, 400)
        self.assertIsNone(transaction)
        self.assertEqual(response_dict.get('amount')[0],"amount can't have a negative value and you input -1000.00")

    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_transaction_info(self,  authenticate_function):
        account = create_test_user()
        now = timezone.now()
        authenticate_function.return_value = account, None
        deposit1 = create_test_transaction(account=account, amount= 100)
        withdrwal1 = create_test_transaction(account=account, 
        amount=90,
        transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL)

        deposit2 = create_test_transaction(account=account, amount= 80)
        withdrwal2 = create_test_transaction(account=account, 
        amount=10,
        transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL)
        url = reverse("transaction:account-statement", kwargs={"account_number":account.account_number})

        response = self.client.get(url)
        response_dict = response.json()
        self.assertEqual(response_dict[0]['accountBalance'], 100)
        self.assertEqual(response_dict[1]['accountBalance'], 10)
        self.assertEqual(response_dict[2]['accountBalance'], 90)
        self.assertEqual(response_dict[3]['accountBalance'], 80)
        