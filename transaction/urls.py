from django.urls import path

from . import views
app_name="transaction"

urlpatterns = [
   
    path('withdrawal/',  views.WithdrawView.as_view(), name="withdrawal"),
    path('deposit/', views.DepositView.as_view(), name="deposit"),
    path('account-statement/<int:account_number>/', views.AccountInfoView.as_view(), name="account-statement" ),
]
