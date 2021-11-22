from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import AdvisorSerializer
from .models import Advisor
# Create your views here.

class AdvisorViewClass(APIView):
    #ModelViewSet is a special view it will handle GET and POST for Advisor
    def post(self, request):
        serializedData = AdvisorSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)




