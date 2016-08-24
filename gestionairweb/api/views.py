from django.db.models import Count, Max, Sum, Q
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import list_route, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from gestionairweb.api.models import Score, Event
from gestionairweb.callcenter.models import Language, Game, Question, Department, Player
from gestionairweb.api.serializers import LanguageSerializer, GameSerializer,\
    DepartmentSerializer, QuestionSerializer, GameDetailSerializer, GamePlayerSerializer, ScoreSerializer, \
    EventSerializer
import random
import datetime
from django.views.decorators.csrf import csrf_exempt


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = GamePlayerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class QuestionViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    queryset = Question.objects.all()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def list(self, request):
        return Response('list not implemented use with an id')

    def retrieve(self, request, pk=None, format=None):
        question = QuestionSerializer(self.queryset.get(number=pk)).data
        question['translations'] = [(x['language'], x['text']) for x in question['translations']]
        return Response(question)

    def create(self, request):
        done_list = request.data['done'] if 'done' in request.data else []
        ret = {}
        questions_list = self.queryset.exclude(number__in=done_list)
        question = random.choice(questions_list)
        ret['next'] = QuestionSerializer(question).data
        if 'answer' in request.data and 'id' in request.data:
            ret['correct'] = Question.objects.get(number=request.data['id'])\
                                 .department.number == request.data['answer']

        return Response(ret)


class GameViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()

    def list(self, request):
        if 'date' in request.query_params:
            date = request.query_params['date'].split('-')
            games = self.queryset.exclude(end_time__isnull=True,
                                          canceled=True)\
                .filter(start_time__year=date[0],
                        start_time__month=date[1],
                        start_time__day=date[2])\
                .annotate(num_players=Count('players'),
                          score_max=Max('players__score'),
                          score_total=Sum('players__score'))\
                .order_by('start_time')

            return Response(GameSerializer(games, many=True).data)
        else:
            return Response({'error': 'provide a date parameter'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None,format=None):
        game = GameDetailSerializer(self.queryset.get(id=pk)).data
        return Response(game)


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    # protect easy download of full scores
    def get_permissions(self):
        if self.action in ('list',):
            self.permission_classes = [IsAdminUser, ]
        return super(self.__class__, self).get_permissions()


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @list_route(methods=['GET'], url_path='upcoming')
    def upcoming(self, request):
        now = datetime.datetime.now()
        events = self.queryset.exclude(Q(end_date__lt=now) | Q(start_date__lt=now, end_date__isnull=True))\
            .order_by('start_date')
        return Response(EventSerializer(events, many=True).data)
