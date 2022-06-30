from unittest import mock
from django.test import TestCase
from django.urls import reverse
from core.tests.models_setups import create_test_user

from user.models import User

# Create your tests here.

class TestUserRegistration(TestCase):

 # 1 user

    def test_user_right_information(self):
        
        url = reverse("user:create_account")
        data= {"account_name":"i@i.com", "password": "new_password", 'initial_deposit':100}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        account = User.objects.first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(),1)
        self.assertTrue(User.objects.filter(username=data.get("account_name")).exists())
        self.assertEquals(len(str(account.account_number)),10)

    def test_user_login(self):
        user = create_test_user(username="odeyemi", password="odeyemi")
        url = reverse("token_obtain_pair")
        data= {"username":"odeyemi", "password": "odeyemi"}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        
    @mock.patch('core.authentication.TokenAuthentication.authenticate')
    def test_user_account_info(self,  authenticate_function):
        user = create_test_user(username="odeyemi", password="odeyemi")
        authenticate_function.return_value = user, None
        url = reverse("user:account-info", kwargs={"account_number":user.account_number})
        response = self.client.get(url)
        response_dict = response.json()
        print(response_dict)
        
    
       