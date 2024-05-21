# services.py
import requests
from .exceptions import CustomException

class PokemonService:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/pokemon'

    def get_pokemon_list(self, offset=0, limit=20):
        try:
            response = requests.get(f'{self.base_url}?offset={offset}&limit={limit}')
            response.raise_for_status()
            
            result = response.json()
            
            return result
        except requests.exceptions.HTTPError as errh:
            raise CustomException("Http Error") from errh
        except requests.exceptions.ConnectionError as errc:
            raise CustomException("Error Connecting") from errc
        except requests.exceptions.Timeout as errt:
            raise CustomException("Timeout Error") from errt
        except requests.exceptions.RequestException as err:
            raise CustomException("Something went wrong") from err