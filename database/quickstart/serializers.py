from .models import Pflege
from rest_framework import serializers


class PflegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pflege
        fields = ('id', 'date', 'time', 'reciever' , 'content')
