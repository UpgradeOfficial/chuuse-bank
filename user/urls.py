
from django.urls import path
from . import views

app_name ="user"

urlpatterns = [
    path(
        'create-account/',
        views.UserRegistrationView.as_view(),
        name="create_account"
    ),
   
]
