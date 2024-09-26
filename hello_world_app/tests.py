from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

class Hello_Test(APITestCase):
    def test_hello_world(self):
        url = '/hello/' # Name used in the URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Hello World"})