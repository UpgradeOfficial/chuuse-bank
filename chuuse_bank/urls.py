from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.views import redirect_to_swagger
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from user.views import MyTokenObtainPairView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from user.views import LoginView

urlpatterns = [
    # YOUR PATTERNS For API Documentation 
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('', redirect_to_swagger),
    path('', include('user.urls')),
    path('', include('transaction.urls')),

    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]


admin.site.site_header = "Chuuse Bank Admin"
admin.site.site_title = "Your Admin Portal"
admin.site.index_title = "Welcome to Chuuse Bank Admin Portal"

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
