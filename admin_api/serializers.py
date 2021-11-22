# Import the Hero model
# Import the REST Framework serializer
# Create a new class that links the Hero with its serializer

from .models import Advisor
from rest_framework import serializers 

class AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id', 'advisor_name', 'photo_url')
