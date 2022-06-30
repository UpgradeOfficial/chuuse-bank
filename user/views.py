from rest_framework import generics, parsers
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, AccountProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from .models import User

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
class UserRegistrationView(generics.CreateAPIView):
    # this can be tested in postman with the form-data
    # Use form data in the client part also
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class AccountInfoView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = AccountProfileSerializer
    queryset = User.objects.all()
    lookup_field = "account_number"
