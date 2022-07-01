from email import message
from core.validators import validate_amount
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
            order__lte=obj.order,
            transaction_type=Transaction.TRANSACTION_TYPE.DEPOSIT).aggregate(sum=Sum('amount'))['sum'] or 0
        total_withdrawal = Transaction.objects.filter(
            account=user, 
            order__lte=obj.order,
            transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL).aggregate(sum=Sum('amount'))['sum'] or 0
        total_balance = total_deposit - total_withdrawal
        return total_balance

        # Date transactionDate
        # String transactionType(Deposit or Withdrawal)
        # String narration
        # Double amount
        # Double accountBalance (after the transaction)


class DepositTransactionSerializer(serializers.Serializer):
    accountNumber = serializers.CharField(write_only=True)
    amount= serializers.DecimalField(max_digits=100, decimal_places=2, write_only=True, validators =[validate_amount],)


    def validate(self,data):
        user = self.context.get('request').user
        accountNumber =data.get("accountNumber")
        amount =data.get("amount")
        account = User.objects.filter(account_number=accountNumber)
        if len(account) == 0 or  user != account.first():
            raise ValidationError("Either account doesn't exist or you are not the owner of this account")
        transaction = Transaction.objects.create(account=user, amount=amount)
        return data

class WithdrawalTransactionSerializer(serializers.Serializer):
    accountNumber = serializers.CharField(write_only=True)
    accountPassword = serializers.CharField(write_only=True)
    withdrawnAmount = serializers.DecimalField(max_digits=100,validators =[validate_amount], decimal_places=2, write_only=True)


    def validate(self, data):
        user = self.context.get('request').user
        accountNumber = data.get("accountNumber")
        accountPassword = data.get("accountPassword")
        withdrawnAmount = data.get("withdrawnAmount")
        account = User.objects.filter(account_number=accountNumber)
        if len(account) == 0 or  user != account.first():
            raise ValidationError("Either account doesn't exist or you are not the owner of this account")
        if not user.check_password(accountPassword):
            raise ValidationError("Password not correct")
        total_deposit = Transaction.objects.filter(account=user, transaction_type=Transaction.TRANSACTION_TYPE.DEPOSIT).aggregate(sum=Sum('amount'))['sum'] or 0
        total_withdrawal = Transaction.objects.filter(account=user, transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL).aggregate(sum=Sum('amount'))['sum'] or 0
        total_balance = total_deposit - total_withdrawal
        if total_balance<=0 or total_deposit< withdrawnAmount:
            raise ValidationError(f"Your account balance is not enough to withdrawn this sum, balance is {total_balance}")
        transaction = Transaction.objects.create(account=user, amount=withdrawnAmount, transaction_type=Transaction.TRANSACTION_TYPE.WITHDRAWAL)
        return data