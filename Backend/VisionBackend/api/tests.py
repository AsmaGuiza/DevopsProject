from django.test import TestCase, Client
from django.urls import reverse
from .models import AIModel
import json

class BasicAIAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_returns_empty_list(self):
        
        
        response = self.client.get("http://127.0.0.1:8000/api/models/")

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertEqual(data, [])

    def test_create_model(self):
        # Data to send in POST request
        data = {
            'name': 'New Model',
            'description': 'Description of the new model',
            'f1_score': 0.8,
            'accuracy':0.9
        }
        
        # Send POST request to create a new model instance
        response = self.client.post("http://127.0.0.1:8000/api/models/", data=data)
        
        # Assert status code is 201 (Created)
        self.assertEqual(response.status_code, 201)
        
        # Assert that the newly created model is returned in the response
        self.assertEqual(json.loads(response.content)['name'], 'New Model')
    def test_retrieve_model(self):
        # Create a model instance
        new_model = AIModel.objects.create(name='Test Model', description='Description of the test model',f1_score=0.8,accuracy=0.8)
        new_model.save()
        new_model_id = new_model.id
        print(new_model_id)
        # Send GET request to retrieve the newly created model
        response = self.client.get(f'http://127.0.0.1:8000/api/models/{new_model_id}/')
         
        # Assert status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Assert that the retrieved model's name matches the created model's name
        self.assertEqual(json.loads(response.content)['name'], 'Test Model')

