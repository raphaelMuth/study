from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.settings import api_settings
from ..serializers.customtokenserializer import CustomTokenSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer
    
    def validate(self, attrs):
        data = super().validate(attrs)

        # Validate issuer
        if data['token']['iss'] != api_settings.SIMPLE_JWT['ISSUER']:
            raise InvalidToken('Invalid issuer')

        # Validate audience
        if data['token']['aud'] != api_settings.SIMPLE_JWT['AUDIENCE']:
            raise InvalidToken('Invalid audience')

        return data