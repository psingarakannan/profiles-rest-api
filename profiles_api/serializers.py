from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer to serialize the API data"""

    name = serializers.CharField(max_length=10)
