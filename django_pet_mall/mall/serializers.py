from rest_framework import serializers
from mallapi.models import Student

class BasicModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = ('name',)
                
class BulkCreateSerializer(serializers.ListSerializer):
            child = BasicModelSerializer()

class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
        list_serializer_class = BulkCreateSerializer
        # fields = ["name", "id"]
