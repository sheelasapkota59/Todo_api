from rest_framework import serializers
from . models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:  
           model = Task    #we need to know which model we want to serialize
           fields = '__all__'    #we need to know how many field we want to display.
                              
