from unittest import mock
from django.test import TestCase
from django.urls import reverse
from core.tests.models_setups import create_test_transaction, create_test_user
from transaction.models import Transaction

from user.models import User

# Create your tests here.

class TestUserRegistration(TestCase):

 # 1 user

    def test_user_right_information(self):
        
        url = reverse("user:create_account")
        data= {"accountName":"i@i.com", "accountPassword": "newPassword", 'initialDeposit':500}
        
        response = self.client.post(url, data=data)
        response_dict = response.json()
        account = User.objects.first()
        transaction = Transaction.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(),1)
        self.assertTrue(User.objects.filter(username=data.get("accountName")).exists())
        self.assertTrue(Transaction.objects.filter(account=account).exists())
        self.assertEquals(transaction.amount,500)
        self.assertEquals(len(str(account.account_number)),10)
        self.assertEqual(response_dict.get("responseCode"),200)
        self.assertTrue(response_dict.get("success"))
        self.assertEqual(response_dict.get("message"),f"New Account created Successfully and your account number is {account.account_number}")



    def test_user_login(self):
        user = create_test_user(username="odeyemi", password="odeyemi")
        url = reverse("token_obtain_pair")
        data= {"account_number":user.account_number, "password": "odeyemi"}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_dict.get("accessToken"))
        self.assertTrue(response_dict.get("success"))
        
    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_user_account_info(self,  authenticate_function):
        user = create_test_user(username="odeyemi", password="odeyemi")
        deposit = create_test_transaction(account=user,amount=100)
        withdrawal = create_test_transaction(account=user,amount=10, transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL)
        authenticate_function.return_value = user, None
        url = reverse("user:account-info", kwargs={"account_number":user.account_number})
        response = self.client.get(url)
        response_dict = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict.get("responseCode"), 200)
        self.assertEqual(response_dict.get("success"), True)
        self.assertEqual(response_dict.get("message"),"Successful")
        self.assertEqual(response_dict.get("account")["accountName"], user.username)
        self.assertEqual(response_dict.get("account")['accountNumber'], user.account_number)
        self.assertEqual(response_dict.get("account")["balance"], user.balance)


        
    
       