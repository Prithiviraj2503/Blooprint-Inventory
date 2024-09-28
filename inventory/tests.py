from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from inventory.models import ItemDetails
from django.urls import reverse

class ItemTests(TestCase):
    
    def setUp(self):
        self.create_url = reverse('add_item') 
        self.item = {
            "item_id": 1,
            "item_name": "Test Item",
            "description": "Test Description",
            "category": 1, 
            "barcode": "86458",
            "supplier": "vendor",
            "cost_price": 10.00,
            "selling_price": 15.00,
            "tax": 1.50,
            "date_added": "2024-09-28",
            "last_updated": "2024-09-28",
            "is_active": True
        }

    def testCreateItem(self):
        response = self.client.post(self.create_url, self.item)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ItemDetails.objects.count(), 1)

    def testGetItem(self):
        self.client.post(self.create_url, self.item)
        response = self.client.get(reverse('item_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item_name'], "Test Item")

    def test_UpdateItem(self):
        self.client.post(self.create_url, self.item)
        updated_item = {
            "item_id": 1,
            "item_name": "Updated Test Item",
            "description": "Updated Description",
            "category": 1,
            "barcode": "86458",
            "supplier": "vendor",
            "cost_price": 12.00,
            "selling_price": 18.00,
            "tax": 1.80,
            "date_added": "2024-09-28",
            "last_updated": "2024-09-28",
            "is_active": True
        }
        response = self.client.put(reverse('item_detail', args=[1]), updated_item)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ItemDetails.objects.get(pk=1).item_name, "Updated Test Item")

    def test_DeleteItem(self):
        self.client.post(self.create_url, self.item)
        response = self.client.delete(reverse('item_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ItemDetails.objects.count(), 0)
        
