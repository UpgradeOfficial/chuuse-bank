from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import  ValidationError
from transaction.models import Transaction
from django.db.models import Sum
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['email'] = user.email
        # token['user_type'] = user.user_type
        # ...

        return token

class AccountProfileSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source="username")
    balance = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['account_name','account_number', "balance"]

    def get_balance(self, obj):
        account_number = self.context.get("view").kwargs.get("account_number")
        user = self.context.get("request").user
        account = User.objects.filter(account_number=account_number)
        if len(account) == 0 or  user != account.first():
            raise ValidationError("Either account doesn't exist or you are not the owner of this account")
        total_deposit = Transaction.objects.filter(account=user, transaction_type=Transaction.TRANSACTION_TYPE.DEPOSIT).aggregate(sum=Sum('amount'))['sum'] or 0
        total_withdrawal = Transaction.objects.filter(account=user, transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL).aggregate(sum=Sum('amount'))['sum'] or 0
        total_balance = total_deposit - total_withdrawal
        return total_balance
class UserRegistrationSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(max_length=10, source="username")
    initial_deposit = serializers.DecimalField(max_digits=100 , decimal_places=2, write_only=True)
    class Meta:
        model = User
        fields = ['account_name', 'initial_deposit', 'password']


    def create(self, validated_data):
        username=validated_data.pop('username')
        password=validated_data.pop('password')
        user = User.objects.create_user(username=username, password=password)
        initial_deposit=validated_data.pop('initial_deposit')
        transaction = Transaction.objects.create(account=user, amount=initial_deposit)
        return user