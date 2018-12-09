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

    def test_risk_type_field(self):
        # Set up a risk type
        data = {'title': 'Risk type 1',
                'description': 'A risk type'}
        response = self.client.post('/api/risktype/', data)

        # Create enum Risk type field
        data = {'title': 'Field 1',
                'description': 'Enum is the tough one',
                'field_type': 'enum',
                'required': False,
                'risk_type': 1}
        response = self.client.post('/api/risktypefield/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.RiskTypeField.objects.count(), 1)
        self.assertEqual(models.RiskTypeField.objects.get().title, 'Field 1')
        self.assertEqual(models.RiskTypeField.objects.get().field_type, 'enum')

        # Update
        data['title'] = 'Field one'
        response = self.client.put('/api/risktypefield/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.RiskTypeField.objects.count(), 1)
        self.assertEqual(models.RiskTypeField.objects.get().title, 'Field one')

        # Get
        # Expected fields:
        data['id'] = 1
        data['options'] = []
        response = self.client.get('/api/risktypefield/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

        # List
        response = self.client.get('/api/risktypefield/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [data])

        # Delete
        response = self.client.delete('/api/risktypefield/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.RiskTypeField.objects.count(), 0)

    def test_enum_option(self):
        # Set up a risk type and an enum field
        data = {'title': 'Risk type 1',
                'description': 'A risk type'}
        response = self.client.post('/api/risktype/', data)
        data = {'title': 'Field 1',
                'description': 'Enum is the tough one',
                'field_type': 'enum',
                'required': False,
                'risk_type': 1}
        response = self.client.post('/api/risktypefield/', data)

        # Create enum option
        data = {'name': 'option1',
                'title': 'Option 1',
                'enum_field': 1}
        response = self.client.post('/api/enumoption/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.EnumOption.objects.count(), 1)
        self.assertEqual(models.EnumOption.objects.get().name, 'option1')
        self.assertEqual(models.EnumOption.objects.get().title, 'Option 1')

        # Update
        data['title'] = 'Option one'
        response = self.client.put('/api/enumoption/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.EnumOption.objects.count(), 1)
        self.assertEqual(models.EnumOption.objects.get().title, 'Option one')

        # Get
        # Expected fields:
        data['id'] = 1
        response = self.client.get('/api/enumoption/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

        # List
        response = self.client.get('/api/enumoption/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [data])

        # Delete
        response = self.client.delete('/api/enumoption/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.EnumOption.objects.count(), 0)

    def test_complex(self):
        data = {'title': 'Risk type 1',
                'description': 'A risk type'}
        response = self.client.post('/api/risktype/', data)
        data = {'title': 'Field 1',
                'description': 'Enum is the tough one',
                'field_type': 'enum',
                'required': False,
                'risk_type': 1}
        response = self.client.post('/api/risktypefield/', data)
        data = {'name': 'option1',
                'title': 'Option 1',
                'enum_field': 1}
        response = self.client.post('/api/enumoption/', data)

        # Get it all
        expected = {
            'id': 1,
            'title': 'Risk type 1',
            'description': 'A risk type',
            'type_fields': [{
                'id': 1,
                'title': 'Field 1',
                'description': 'Enum is the tough one',
                'field_type': 'enum',
                'required': False,
                'risk_type': 1,
                'options': [{
                    'id': 1,
                    'name': 'option1',
                    'title': 'Option 1',
                    'enum_field': 1,
                }]
            }]
         }

        response = self.client.get('/api/risktype/')
        self.assertEqual(response.data, [expected])
