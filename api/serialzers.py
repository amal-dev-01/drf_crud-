from rest_framework import serializers
from api.models import Students


class StudentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Students
        fields = '__all__'


# Not need the create & update methods
# __________________________or______________________________

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField( max_length=50)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=50)


    # def create(self,validate_data):
    #     return Students.objects.create(**validate_data) 

    # def update(self,instance,validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.roll = validated_data.get('roll',instance.roll)
    #     instance.city = validated_data.get('city',instance.city)
    #     instance.save()
    #     return instance


    def validate_roll(self,value):
        if value >= 150:
            raise serializers.ValidationError('Booking Full !!!!!!')
        return value
    def validate_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Name must start with a capital letter.")
        return value
