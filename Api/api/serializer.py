from rest_framework import serializers
from .models import Programmer
 
class ProgrammerSerializer(serializers.ModelSerializer):
     class Meta:
         model = Programmer
         #fields = ('id', 'fullname', 'nickyname', 'age', 'is_activated')
         fields = '__all__'
         