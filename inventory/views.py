from django.shortcuts import render
from inventory.models import ItemDetails
from inventory.serializers import ItemSerializer
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
import logging

#Log Initialize
logger = logging.getLogger(__name__)

class NewItem(APIView):
    permissions_class_list = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Item created: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Error adding item: {serializer.errors}")
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView):

    def get(self, request, pk):
        cachekey = f'item_{pk}' #set unique cache key
        item = cache.get(cachekey)
        if item:
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        else:
            items = get_object_or_404(ItemDetails, pk=pk)
            serializer = ItemSerializer(items)
            cache.set(item, item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        items = get_object_or_404(ItemDetails, pk=pk)
        serializer = ItemSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache_key = f'item_{pk}'
            cache.delete(cache_key)
            return Response(serializer.data)
        logger.info(f"Error in update: {serializer.data}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        item = get_object_or_404(ItemDetails, pk=pk)
        item.delete()
        cache_key = f'item_{pk}'
        cache.delete(cache_key)
        logger.info(f"Item deleted: {pk}")
        return Response(status=status.HTTP_204_NO_CONTENT)



    

    

