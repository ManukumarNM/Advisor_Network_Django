# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer, BookingSerializer, LoginSerializer
from admin_api.serializers import AdvisorSerializer
from admin_api.models import Advisor
from .models import User, Booking
# from django.contrib import auth
# import jwt
# from django.contrib.auth import authenticate, login

# from rest_framework_jwt.settings import api_settings

# # # Get the JWT settings
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.
class UserRegisterClassView(APIView):
    def post(self, request):
        user_name = request.data["user_name"]
        user_email = request.data["user_email"]
        user_password = request.data["user_password"]
        saveData = {"user_name":user_name, "user_email":user_email, "user_password":user_password}
        serializedData = UserSerializer(data=saveData)
        if serializedData.is_valid():
            user = serializedData.save()
            return Response({"user_id":user.id}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# class UserLoginClassView(APIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         data = request.data
#         user_email = data.get('user_email', '')
#         user_password = data.get('user_password', '')
#         user = auth.authenticate(user_email=user_email, user_password=user_password)

#         if user:
#             auth_token = jwt.encode(
#                 {'user_email': user.user_email}, settings.JWT_SECRET_KEY, algorithm="HS256")

#             serializer = UserSerializer(user)

#             data = {'user': serializer.data, 'token': auth_token}

#             return Response(data, status=status.HTTP_200_OK)

#             # SEND RESPONSE
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLoginClassView(APIView):
    def post(self, request):
        try:
            user = User.objects.all().filter(user_email=request.data["user_email"])[0]
            password = request.data["user_password"]
            if not (user.user_password == password):
                return Response(status=status.HTTP_401_AUTHENTICATION_ERROR)
            return Response({"user_id": user.id}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class ListAdvisorsView(APIView):
    def get(self, request, id):
        advisors = Advisor.objects.all()
        serialized_data = AdvisorSerializer(advisors, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)


class BookingAdvisorView(APIView):
    def post(self, request, user_id, advisor_id):
        serialized_data = BookingSerializer(data={
            'user':user_id, 
            'advisor':advisor_id, 
            'datetime':request.data["datetime"]
        })
        if serialized_data.is_valid():
            serialized_data.save()
        return Response(status=status.HTTP_200_OK)


class ListBookingsView(APIView):
    def get(self, request, user_id):
        booking = Booking.objects.all().filter(user=user_id)
        serialized_data = BookingSerializer(booking, many=True)
        res = []
        for result in serialized_data.data:
            advisor = Advisor.objects.all().filter(id=result["advisor"])[0]
            values = {
                    "advisor_name": advisor.name,
                    "photo_url": advisor.photo_url,
                    "advisor_id": advisor.id,
                    "booking_id": result["id"],
                    "booking_time": result["datetime"],      
                }
            res.append(values)
        return Response(res, status=status.HTTP_200_OK)
