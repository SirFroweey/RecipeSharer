from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import RequestsClient

from requests.auth import HTTPBasicAuth

from api.models import Recipe, Ingredient, Note

from tests.utils import BASE_URL, build_user, fake_data


class APITests(TestCase):

    def setUp(self):
        # build fake data
        self.user = build_user()
        fake_data(user=self.user['user'])
        # build api client
        self.client = RequestsClient()
        self.client.auth = HTTPBasicAuth(self.user['username'], self.user['password'])
        self.client.headers.update({'x-test': 'true'})

    def test_listapiview_should_pass(self):
        request = self.client.get(f'{BASE_URL}/api/recipe/list')
        response = request.json()
        self.assertEqual(len(response), 100)
        self.assertEqual(len(response[0]['ingredients']), 1)
        self.assertEqual(len(response[0]['notes']), 1)

    def test_get_recipe_endpoint_should_pass(self):
        request = self.client.get(f'{BASE_URL}/api/recipe/1')
        response = request.json()
        self.assertTrue(isinstance(response, dict) and len(response['name']))
        self.assertEqual(len(response['ingredients']), 1)
        self.assertEqual(len(response['notes']), 1)
