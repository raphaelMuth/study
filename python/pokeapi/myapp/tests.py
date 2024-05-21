from django.test import TestCase
import requests
# Create your tests here.
# test_services.py
from .services import PokemonService
import requests_mock
import json
import os
from .exceptions import CustomException

class PokemonAPITestCase(TestCase):
    
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'list_mock_data.json')) as f:
            self.mock_data = json.load(f)

        self.mocker = requests_mock.Mocker()
        self.mocker.start()

    def tearDown(self):
        self.mocker.stop()
        self.mocker.reset()

    def test_get_pokemon_list(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', json=self.mock_data)
        service = PokemonService()
        result = service.get_pokemon_list()
        self.assertIn({"name":"pidgeot","url":"https://pokeapi.co/api/v2/pokemon/18/"}, result['results'])

    def test_get_pokemon_list_connection_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', exc=requests.exceptions.ConnectionError) 
        with self.assertRaisesMessage(CustomException, 'Error Connecting'):
            service = PokemonService()
            result = service.get_pokemon_list()
    
    def test_get_pokemon_list_timeout_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', exc=requests.exceptions.Timeout) 
        with self.assertRaisesMessage(CustomException, 'Timeout Error'):
            service = PokemonService()
            result = service.get_pokemon_list()

    def test_get_pokemon_list_unspecified_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', exc=requests.exceptions.RequestException) 
        with self.assertRaisesMessage(CustomException, 'Something went wrong'):
            service = PokemonService()
            result = service.get_pokemon_list()

    def test_get_pokemon_list_http_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', status_code=404)
        with self.assertRaisesMessage(CustomException, 'Http Error'):
            service = PokemonService()
            result = service.get_pokemon_list()