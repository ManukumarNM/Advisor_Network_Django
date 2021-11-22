from django.urls import path
from .views import UserRegisterClassView, UserLoginClassView, ListAdvisorsView, BookingAdvisorView, ListBookingsView

urlpatterns = [
    path('register/', UserRegisterClassView.as_view()), #http://127.0.0.1:8000/user/register/
    path('login/', UserLoginClassView.as_view()),       #http://127.0.0.1:8000/user/login/
    path('<int:id>/advisor/', ListAdvisorsView.as_view()), #http://127.0.0.1:8000/user/1/advisors/
    path('<int:user_id>/advisor/<int:advisor_id>/', BookingAdvisorView.as_view()), #http://127.0.0.1:8000/user/1/advisor/1/
    path('<int:user_id>/advisor/booking/', ListBookingsView.as_view()), #http://127.0.0.1:8000/user/1/advisor/booking/
]