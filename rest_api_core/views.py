from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer

class HelloAPIView(APIView):
    """Class for handling the API View"""
    def get(self, request):
        return Response({"success":True, "data": "Hello, API apprentice!!!"})
    
    def post(self, request):
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = serializer.validated_data.get('message')
            
            return Response({"success":True, "data":serializer.validated_data, "message": f"Hello, {name} \n {message}"}, status=status.HTTP_200_OK)            
        
        return Response({"success":False, "data":serializer.errors, "message": "Validation Failed!" }, status=status.HTTP_400_BAD_REQUEST)
        