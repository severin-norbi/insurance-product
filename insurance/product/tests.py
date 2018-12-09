from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from . import models


class ProductAPITests(APITestCase):

    def setUp(self):
        self.username = "test"
        self.email = "test@test.ts"
        self.password = "secret"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.client.login(username=self.username, password=self.password)

    def test_risk_type(self):
        # Create
        data = {'title': 'Risk type 1',
                'description': 'A risk type'}
        response = self.client.post('/api/risktype/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.RiskType.objects.count(), 1)
        self.assertEqual(models.RiskType.objects.get().title, 'Risk type 1')

        # Update
        data = {'title': 'Risk type one',
                'description': 'An updated risk type'}
        response = self.client.put('/api/risktype/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.RiskType.objects.count(), 1)
        self.assertEqual(models.RiskType.objects.get().title, 'Risk type one')

        # Get
        # Expected fields:
        data['id'] = 1
        data['type_fields'] = []
        response = self.client.get('/api/risktype/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

        # List
        response = self.client.get('/api/risktype/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [data])

        # Delete
        response = self.client.delete('/api/risktype/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.RiskType.objects.count(), 0)
