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
        result = PokemonService().get_pokemon_list()
        self.assertIn({"name":"pidgeot","url":"https://pokeapi.co/api/v2/pokemon/18/"}, result['results'])

    def test_get_pokemon_list_connection_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', exc=requests.exceptions.ConnectionError) 
        with self.assertRaisesMessage(CustomException, 'Error Connecting'): 
            result = PokemonService().get_pokemon_list()
    
    def test_get_pokemon_list_timeout_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', exc=requests.exceptions.Timeout) 
        with self.assertRaisesMessage(CustomException, 'Timeout Error'): 
            result = PokemonService().get_pokemon_list()

    def test_get_pokemon_list_unspecified_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', exc=requests.exceptions.RequestException) 
        with self.assertRaisesMessage(CustomException, 'Something went wrong'): 
            result = PokemonService().get_pokemon_list()

    def test_get_pokemon_list_http_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon', status_code=404)
        with self.assertRaisesMessage(CustomException, 'Http Error'): 
            result = PokemonService().get_pokemon_list()


    def test_get_pokemon_by_name_success(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon/1', json={'name': 'bulbasaur'})
        result = PokemonService().get_pokemon_by_name(1)
        self.assertEqual(result, {'name': 'bulbasaur'})

    def test_get_pokemon_by_name_http_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon/1', status_code=404)
        with self.assertRaises(CustomException) as cm:
            PokemonService().get_pokemon_by_name(1)
        self.assertEqual(str(cm.exception), 'Http Error')

    def test_get_pokemon_by_name_connection_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon/1', exc=requests.exceptions.ConnectionError)
        with self.assertRaises(CustomException) as cm:
            PokemonService().get_pokemon_by_name(1)
        self.assertEqual(str(cm.exception), 'Error Connecting')

    def test_get_pokemon_by_name_timeout_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon/1', exc=requests.exceptions.Timeout)
        with self.assertRaises(CustomException) as cm:
            PokemonService().get_pokemon_by_name(1)
        self.assertEqual(str(cm.exception), 'Timeout Error')

    def test_get_pokemon_by_name_generic_error(self): 
        self.mocker.get('https://pokeapi.co/api/v2/pokemon/1', exc=requests.exceptions.RequestException)
        with self.assertRaises(CustomException) as cm:
            PokemonService().get_pokemon_by_name(1)
        self.assertEqual(str(cm.exception), 'Something went wrong')