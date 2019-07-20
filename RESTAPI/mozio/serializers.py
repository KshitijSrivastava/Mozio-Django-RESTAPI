from rest_framework import serializers
from mozio.models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['name', 'email', 'phone_number', 'phone_number', 'language', 'currency']
