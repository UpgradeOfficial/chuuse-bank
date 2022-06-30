
from django.urls import path
from . import views

app_name ="user"

urlpatterns = [
    path(
        'create-account/',
        views.UserRegistrationView.as_view(),
        name="create_account"
    ),
    path('account-info/<int:account_number>/', views.AccountInfoView.as_view(), name= "account-info"),
    
   
]
