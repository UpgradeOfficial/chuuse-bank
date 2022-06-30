
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from transaction.models import Transaction
from user.models import User
from rest_framework.exceptions import  ValidationError
from . import serializers
import transaction

# Create your views here.
class WithdrawView(CreateAPIView):
    serializer_class = serializers.WithdrawalTransactionSerializer

class DepositView(CreateAPIView):
    serializer_class = serializers.DepositTransactionSerializer

class AccountInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, *args, **kwargs):
        user = self.request.user
        account_number = kwargs.get("account_number")
        account = User.objects.filter(account_number=account_number)
        if len(account) == 0 or  user != account.first():
            raise ValidationError("Either account doesn't exist or you are not the owner of this account")
        transactions = Transaction.objects.filter(account=user)
        transaction_serializer = serializers.TransactionInfoSerializer(transactions, context={"request":self.request}, many=True)
        return Response(data=transaction_serializer.data)
