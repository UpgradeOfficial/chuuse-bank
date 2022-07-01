from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import  ValidationError
from transaction.models import Transaction
from .serializers import LoginSerializer, UserRegistrationSerializer, AccountProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token
from .serializers import MyTokenObtainPairSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
class UserRegistrationView(APIView):
    # this can be tested in postman with the form-data
    # Use form data in the client part also
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        accountName = serializer.validated_data.get('accountName')
        accountPassword = serializer.validated_data.get('accountPassword')
        initialDeposit = serializer.validated_data.get('initialDeposit')
        user = User.objects.create_user(username=accountName, password=accountPassword)
       
        transaction = Transaction.objects.create(account=user, amount=initialDeposit)
        data ={
            "responseCode":200,
            'success': True,
            "message": f"New Account created Successfully and your account number is {user.account_number}"
        }
        

        return Response(data=data)

class LoginView(ObtainAuthToken):
    # this can be tested in postman with the form-data
    # Use form data in the client part also
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data, context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={"accessToken": token.key, "success":True})
        

class AccountInfoView(APIView): 
    serializer_class = AccountProfileSerializer
    
    
    def get(self, *args, **kwargs):
        account_number = kwargs.get("account_number")
        user = self.request.user
        account = User.objects.filter(account_number=account_number)
        if  account.exists() is False or  user != account.first():
            raise ValidationError("Either account doesn't exist or you are not the owner of this account")
        user = self.request.user
        data = {
        "responseCode":200,
        "success":True,
        "message" : "Successful",
        "account": {
        "accountName": user.username,
        "accountNumber":user.account_number,
        "balance": user.balance
            }
        }
        return Response(data=data)



