from rest_framework import serializers
from Genericapp .models import Emp


class Empserializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ('eid','ename','esal')
