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
class UserRegistrationSerializer(serializers.Serializer):
    accountName = serializers.CharField(max_length=100)
    accountPassword  = serializers.CharField(max_length=100, write_only=True)
    initialDeposit = serializers.DecimalField(max_digits=100 , decimal_places=2, write_only=True)
    
    def validate(self, attrs):
        accountName=attrs.get("accountName")
        accountPassword=attrs.get("accountPassword")
        initialDeposit=attrs.get("initialDeposit")
        users=User.objects.filter(username=accountName)
        if users.exists():
            raise ValidationError("user with this account name already does exists")
        user = users.first()
        if len(accountPassword)<8:
            raise ValidationError("Password must be getter than 8 characters")
        if initialDeposit<500:
            raise ValidationError("Initial Deposit must be greater or equals to 500")
        return attrs


    # def create(self, validated_data):
    #     username=validated_data.pop('accountName')
    #     password=validated_data.pop('password')
    #     user = User.objects.create_user(username=username, password=password)
    #     initial_deposit=validated_data.pop('initial_deposit')
    #     transaction = Transaction.objects.create(account=user, amount=initial_deposit)
    #     return user

class LoginSerializer(serializers.Serializer):
    account_number = serializers.IntegerField( write_only=True)
    password = serializers.CharField(max_length=10, write_only=True)
    
    def validate(self, attrs):
        account_number=attrs.get("account_number")
        password=attrs.get("password")
        users=User.objects.filter(account_number=account_number)
        if not users.exists():
            raise ValidationError("user with this account number doesn't exists")
        user = users.first()
        password_match = user.check_password(password)
        if not password_match:
            raise ValidationError("Incorrect Password")
        attrs['user'] = user
        return attrs
        # Apply custom validation either here, or in the view.
