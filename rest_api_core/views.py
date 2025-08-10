from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"success":True, "message": "Hello, API apprentice!!!"})
    
    def post(self, request):
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = serializer.validated_data.get('message')
            
            return Response({"success":True, "message": f"Hello, {name} \n {message}"}, status=status.HTTP_200_OK)            
        
        return Response({"success":False, "message": "Name is required!" }, status=status.HTTP_400_BAD_REQUEST)
        