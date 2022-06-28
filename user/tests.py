import os
from unittest import mock
from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from core.tests.models_setups import create_test_class_room, create_test_user

from user.models import User

# Create your tests here.

class TestUserRegistration(TestCase):

    def setUp(self):
        #this is needed to hash the password
        #create user will not hash the password
        # self.user = User.objects.create_user(email="odeyemiincrease@yahoo.c", password='password')
        self.user = create_test_user() # 1 user

    def test_user_right_information(self):
        
        url = reverse("user:create_account")
        data= {"account":"i@i.com", "password": "new_password", 'initial_deposit':100}
        response = self.client.post(url, data=data)
        response_dict = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(),5)
        self.assertEqual(Student.objects.count(),1)
        self.assertTrue(User.objects.filter(email="i@i.com").exists())
        self.assertTrue('tokens' in response_dict)
        self.assertTrue('access' in response_dict["tokens"])
        self.assertTrue('refresh' in response_dict["tokens"])
        link = (
            "/".join(
                [
                    settings.FRONTEND_URL,
                    "api",
                    "user"
                    "email-verification",
                    ExpiringActivationTokenGenerator().generate_token(student.user.email).decode('utf-8')
                ]
            )
        )
        base_url =  settings.BACKEND_BASE_URL
        context = {
        "site": "Logg",
        "MEDIA_URL": "/".join((base_url, settings.MEDIA_URL[1:-1])),
        "name": student.user.first_name or student.user.email,
        "link": link   
        }
        template_name = "account_verification.html"
        email_html_body = render_to_string(template_name, context)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Welcome to Logg, please verify your email address")
        self.assertEqual(mail.outbox[0].from_email, settings.EMAIL_HOST_USER)
        self.assertEqual(mail.outbox[0].to[0], student.user.email)
        # with open('index.html', 'w') as f:
        #     f.write(mail.outbox[0].body)
        # print(mail.outbox[0].body)
        # self.assertTrue(ExpiringActivationTokenGenerator().generate_token(student.user.email).decode('utf-8') in mail.outbox[0].body )
        #self.assertEqual(mail.outbox[0].body, email_html_body)
        #check if password is hashed
        self.assertNotEqual(data['password'], User.objects.first().password)