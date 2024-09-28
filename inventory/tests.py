from django.test import TestCase
from rest_framework.test import APIClient
from inventory.models import ItemDetails

class ItemTest(TestCase):
    def TestSetup(self):
        self.client =  APIClient()

    def getitem(self):
        items = self.client.get('/api/items/')
        self.assertEqual(response.status_code, 200)
        
