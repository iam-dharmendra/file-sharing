from django.db.models import fields
from rest_framework import serializers
from .models import showdata, testserial,InvoiceToDB,Plo

class Poi(serializers.ModelSerializer):
    class Meta:
        model=testserial
        fields='__all__'
        #fields=['field1','field2','field3']


class Csvserializer(serializers.ModelSerializer):
    class Meta:
        model=showdata
        fields='__all__'
        #fields=['field1','field2','field3']


class Invoicesrializer(serializers.ModelSerializer):
    class Meta:
        model=InvoiceToDB
        fields='__all__'
        #fields=['field1','field2','field3']
        
class DemoSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    class Meta:
        model=Plo
        # fields='__all__'
        fields='__all__'
class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plo
        fields = ['company','file']