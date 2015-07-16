from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from gestionairweb.callcenter.models import Language, Game, Player
from gestionairweb.api.serializers import LanguageSerializer, GameSerializer, GamePlayerSerializer
# Create your views here.


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = GamePlayerSerializer


class GameViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()

    def list(self, request):
        return Response('list not implemented use with an id')

    def retrieve(self, request, pk=None,format=None):
        game = GameSerializer(self.queryset.get(id=pk)).data
        return Response(game)