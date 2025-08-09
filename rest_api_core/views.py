from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"success":True, "message": "Hello, API apprentice!!!"})
    
    def post(self, request):
        name = request.data.get('name')
        message = request.data.get('message')
        if not name:
            return Response({"success":False, "message": "Name is required!" })
        return Response({"success":True, "message": f"Hello, {name} \n {message}"})