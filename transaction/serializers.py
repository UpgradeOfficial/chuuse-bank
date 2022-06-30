from email import message
from rest_framework import serializers
from user.models import User
from .models import Transaction
from rest_framework.exceptions import  ValidationError
from django.db.models import Sum
from transaction.models import Transaction

class TransactionInfoSerializer(serializers.ModelSerializer):
    transactionDate = serializers.DateTimeField(source="created_at")
    transactionType = serializers.CharField(source="transaction_type")
    accountBalance =  serializers.SerializerMethodField(read_only=True)
    narration =  serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Transaction
        fields = ['transactionDate', 'transactionType',"narration", "amount", "accountBalance", ]

    def get_narration(self, obj):
        narration = f"This {obj.transaction_type} was made on {obj.created_at.strftime('%Y-%d-%m')}"
        return narration

    def get_accountBalance(self, obj):
        user = self.context.get("request").user
        total_deposit = Transaction.objects.filter(
            account=user,
            created_at__lte=obj.created_at,
            transaction_type=Transaction.TRANSACTION_TYPE.DEPOSIT).aggregate(sum=Sum('amount'))['sum'] or 0
        total_withdrawal = Transaction.objects.filter(account=user, created_at__gte=obj.created_at ,transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL).aggregate(sum=Sum('amount'))['sum'] or 0
        total_balance = total_deposit - total_withdrawal
        #print(total_deposit,total_withdrawal, total_balance,total_balance)
        return total_balance

        # Date transactionDate
        # String transactionType(Deposit or Withdrawal)
        # String narration
        # Double amount
        # Double accountBalance (after the transaction)


class DepositTransactionSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(write_only=True)
    class Meta:
        model = Transaction
        fields = ['account_number', 'amount']
        # exclude = ['groups','user_permissions', 'auth_povider'] + User.get_hidden_fields()
        read_only_fields = ("account", "transaction_type")
        # extra_kwargs = {
        #     'user_type': {'write_only': True},
            
        # }

    def create(self, validated_data):
        user = self.context.get('request').user
        account_number = validated_data.get("account_number")
        amount = validated_data.get("amount")
        account = User.objects.filter(account_number=account_number)
        if len(account) == 0 or  user != account.first():
            raise ValidationError("Either account doesn't exist or you are not the owner of this account")
        transaction = Transaction.objects.create(account=user, amount=amount)
        return transaction

class WithdrawalTransactionSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(write_only=True)
    class Meta:
        model = Transaction
        fields = "__all__"
        # exclude = ['groups','user_permissions', 'auth_povider'] + User.get_hidden_fields()
        read_only_fields = ("account", "transaction_type")
        # extra_kwargs = {
        #     'user_type': {'write_only': True},
            
        # }

    def create(self, validated_data):
        user = self.context.get('request').user
        account_number = validated_data.get("account_number")
        amount = validated_data.get("amount")
        account = User.objects.filter(account_number=account_number)
        if len(account) == 0 or  user != account.first():
            raise ValidationError("Either account doesn't exist or you are not the owner of this account")
        total_deposit = Transaction.objects.filter(account=user, transaction_type=Transaction.TRANSACTION_TYPE.DEPOSIT).aggregate(sum=Sum('amount'))['sum'] or 0
        total_withdrawal = Transaction.objects.filter(account=user, transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL).aggregate(sum=Sum('amount'))['sum'] or 0
        total_balance = total_deposit - total_withdrawal
        if total_balance<=0 or total_deposit< amount:
            raise ValidationError(f"Your account balance is not enough to withdrawn this sum, balance is {total_balance}")
        transaction = Transaction.objects.create(account=user, amount=amount, transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL)
        return transaction