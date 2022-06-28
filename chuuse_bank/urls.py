from django.contrib import admin
from django.urls import path, include
from core.views import redirect_to_swagger
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # YOUR PATTERNS For API Documentation 
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('', redirect_to_swagger),
    path('', include('user.urls')),
    path('', include('transaction.urls')),
]


admin.site.site_header = "Chuuse Bank Admin"
admin.site.site_title = "Your Admin Portal"
admin.site.index_title = "Welcome to Chuuse Bank Admin Portal"
