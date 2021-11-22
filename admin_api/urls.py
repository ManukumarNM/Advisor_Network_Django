from django.contrib import admin

from django.urls import path
from .views import AdvisorViewClass
# from rest_framework import routers 

# router = routers.DefaultRouter()
# router.register('advisors', views.AdvisorView)

urlpatterns = [
    path('advisor/',AdvisorViewClass.as_view()), #http://127.0.0.1:8000/admin/advisor/
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
]

