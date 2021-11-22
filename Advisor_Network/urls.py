from django.contrib import admin
from django.urls import path, include
#from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('superuser/', admin.site.urls),
    path('admin/', include('admin_api.urls')),
    path('user/',include('user_api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
