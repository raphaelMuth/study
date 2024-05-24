from rest_framework import viewsets
from rest_framework.response import Response
from ..services import PokemonService
from rest_framework.permissions import IsAuthenticated

OFFSET_DEFAULT = 0
LIMIT_DEFAULT = 20
BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'
RESULTS = 'results'
URL = 'url'
NEXT = 'next'
PREVIOUS = 'previous'
COUNT = 'count'

class PokemonViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        service = PokemonService()
        offset = request.query_params.get('offset', OFFSET_DEFAULT)
        limit = request.query_params.get('limit', LIMIT_DEFAULT)
        pokemon_data = service.get_pokemon_list(offset=offset, limit=limit)

        uri_without_params = request.build_absolute_uri().split('?')[0]

        pokemon_list = pokemon_data[RESULTS]
        for item in pokemon_list:
            item[URL] = item[URL].replace(BASE_URL, uri_without_params)

        response = Response(pokemon_list)

        next_link = pokemon_data.get(NEXT)
        if next_link:
            response['X-NEXT-LINK'] = next_link.replace(BASE_URL, uri_without_params)

        previous_link = pokemon_data.get(PREVIOUS)
        if previous_link:
            response['X-PREVIOUS-LINK'] = previous_link.replace(BASE_URL, uri_without_params)
        
        response['X-TOTAL-COUNT'] = pokemon_data.get(COUNT)

        return response
    
    def retrieve(self, request, pk=None):
        service = PokemonService()
        pokemon_data = service.get_pokemon_by_name(pk)
        return Response(pokemon_data)