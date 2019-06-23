from urllib.parse import unquote_plus

from django.conf import settings
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


class VectorsView(APIView):
    def get(self, request):
        word = unquote_plus(request.GET['word'])
        if word is None or word not in settings.VECTORS:
            raise Http404()
        return Response(settings.VECTORS.get(word))
