from rest_framework import serializers
from inventory.models import ItemDetails

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetails
        fields = '__all__'
