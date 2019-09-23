from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIview"""
    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, delete)',
            'Is similiar to the traditional Django View',
            'Gives you the most control over application logic',
            'Is mapped manually to URL',
        ]

        return Response({'message': 'Hello', 'an_apiview' : an_apiview})
        