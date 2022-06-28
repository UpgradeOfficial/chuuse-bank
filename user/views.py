from rest_framework import generics, parsers
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    # this can be tested in postman with the form-data
    # Use form data in the client part also
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
