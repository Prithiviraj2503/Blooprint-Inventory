from django.shortcuts import render
from rest_framework import viewsets
from inventory.models import ItemDetails
from inventory.serializers import ItemSerializer
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import logging

#Log Initialize
applogger = logging.getLogger(__name__)
# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = ItemDetails.objects.all()
    permissions_class_list = [IsAuthenticated]
    def item_list(self, request):
        if 'cache_items' in cache:
            logger.debug(f"Caching items: {items}")
            items = cache.get('cache_items')
        else:
            items = ItemDetails.objects.all()
            logger.debug(f"Select Items items: {items}")
            cache.set('cache_items', items)



