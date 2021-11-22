from .models import User, Booking
from rest_framework import serializers, fields
# cd
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_email', 'user_password')

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    datetime = fields.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S"])
    class Meta:
        model = Booking
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    user_password = serializers.CharField(max_length=200, write_only=True)
    user_email = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['user_email', 'user_password']