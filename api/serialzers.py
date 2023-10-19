from rest_framework import serializers
from api.models import Students



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField( max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)


    def create(self,validate_data):
        return Students.objects.create(**validate_data) 