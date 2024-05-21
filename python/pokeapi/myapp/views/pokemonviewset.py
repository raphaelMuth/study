from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from ..services import PokemonService

class PokemonViewSet(viewsets.ViewSet):
    def list(self, request):
        service = PokemonService()
        offset = request.query_params.get('offset')
        limit = request.query_params.get('limit')
        pokemon_data = service.get_pokemon_list(offset=offset, limit=limit)

        uri_without_params = request.build_absolute_uri().split('?')[0]

        response = Response(pokemon_data['results'])

        next_offset = int(offset) + int(limit)
        if(next_offset < pokemon_data['count']):
            response['X-NEXT-LINK'] = f"{uri_without_params}?offset={next_offset}&limit={limit}"

        previous_offset = int(offset) - int(limit)
        if(previous_offset > 0):
            response['X-PREVIOUS-LINK'] = f"{uri_without_params}?offset={previous_offset}&limit={limit}"

        response['X-TOTAL-COUNT'] = pokemon_data.get('count')
    
        return response