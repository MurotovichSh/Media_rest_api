from django.test import TestCase
from django.contrib.auth.models import User
from oauth2_provider.models import Application
from django.test import Client
import json
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here
class OauthTestCase(TestCase):
# user create 
    def setUp(self):
        self.user = User.objects.create_user(username='random_user', password='random_password')

# new OAuth2 application
        self.app = Application.objects.create(
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            redirect_uris='/',
            name='Test_application',
            client_id='test-id',
            client_secret='test-secret',
)
        print(self.app)

# Fetch the access token from the token endpoint
    def test_token_fetch(self):
        client = Client()
        self.response = client.post(
            '/o/token/',
            {
                'grant_type': 'password',
                'username': 'random_user',
                'password': 'random_password',
                'client_id': 'test-id',
                'client_secret': 'test-secret',
            }
         )



# Parse the response to extract the access token
        response_data = json.loads(self.response.content.decode('utf-8'))
        print(response_data)
        access_token = response_data['access_token']

# Make a request using APIClient and the obtained access token
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = api_client.get('/posts/', format='json')
        assert response.status_code == status.HTTP_200_OK
        self.user.delete()
        self.app.delete()
