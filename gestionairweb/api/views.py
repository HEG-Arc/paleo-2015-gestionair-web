from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from gestionairweb.callcenter.models import Language, Game, Question, Department
from gestionairweb.api.serializers import LanguageSerializer, GameSerializer, DepartmentSerializer, QuestionSerializer
import random


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class QuestionViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    queryset = Question.objects.all()

    def list(self, request):
        return Response('list not implemented use with an id')

    def retrieve(self, request, pk=None,format=None):
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
            ret['correct'] = Question.objects.get(number=request.data['id']).department.number == request.data['answer']

        return Response(ret)


class GameViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()

    def list(self, request):
        return Response('list not implemented use with an id')

    def retrieve(self, request, pk=None,format=None):
        game = GameSerializer(self.queryset.get(id=pk)).data
        return Response(game)