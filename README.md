# Guide to Setting Up Django Backend

This guide will lead you through the process of running the Django backend API for VisualVision. Make sure you have Python and Pipenv installed on your system before you continue.

## Prerequisites

- Python 3.10
- Pipenv

## Installation

1. Clone the repository:

2. Navigate to the project directory:

   ```bash
   cd Backend
   ```

3. Install project dependencies using Pipenv:

   ```bash
   pipenv install -r requirements.txt
   ```

4. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

## Running the Server

1. Apply migrations:
   ```bash
   cd VisionBackend
   ```

   ```bash
   python manage.py migrate
   ```

3. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

4. Open your web browser and go to `http://localhost:8000`. You should either see the default Django landing page or your project's homepage if it's been configured.

## Additional Notes

-To add more Python packages, use Pipenv. Activate the virtual environment with `pipenv shell` before installing packages.

-Keep your virtual environment active (`pipenv shell`) whenever you're working on the project to ensure you're using the right dependencies.

- Don't forget to deactivate the virtual environment once you're done working on the project:

  ```bash
  exit
  ```
#### Testing model creation: The specified test functions can be found in "tests.py".

```python
def test_create_model(self):
    # Données à envoyer dans la requête POST
    data = {
        'name': 'New Model',
        'description': 'Description du nouveau modèle'
        # Inclure d'autres champs si nécessaire
    }
    
    # Envoie une requête POST pour créer une nouvelle instance de modèle
    response = self.client.post(reverse('model-list'), data=data)
    
    # Vérifie que le code d'état est 201 (Créé)
    self.assertEqual(response.status_code, 201)
    
    # Vérifie que le modèle nouvellement créé est renvoyé dans la réponse
    self.assertEqual(json.loads(response.content)['name'], 'New Model')
===============================================================================================
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
===============================================================================================

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

```

- To deploy your Django applications for production, consult the Django documentation for guidance on production deployments.

## Troubleshooting

- Should you encounter any difficulties during the installation or setup process, don't hesitate to open an issue on the project repository or reach out to the project maintainers for support.
