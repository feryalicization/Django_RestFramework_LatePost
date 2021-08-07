from django.db.models import fields
from rest_framework import serializers
from .models import List_orderan

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_orderan
        fields = '__all__'