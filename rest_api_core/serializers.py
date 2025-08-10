from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length = 50)
    message = serializers.CharField(required=False, max_length=200, allow_blank=True)