from rest_framework import serializers
from gestionairweb.callcenter.models import Language, Game, Player, Answer, Question, Translation, Department
from gestionairweb import settings
from .models import Score, Event, Statistic


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language

    flag = serializers.SerializerMethodField()

    def get_flag(self, obj):
        return '%s%s' % (settings.STATIC_URL, obj.flag)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('language', 'text')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('number', 'translations')
    translations = TranslationSerializer(many=True, read_only=True)


class PlayerAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('sequence', 'correct', 'answer')

    def to_representation(self, instance):
        ret = super(serializers.ModelSerializer, self).to_representation(instance)
        translation = instance.question
        ret['question'] = translation.question.number
        ret['code'] = translation.language.code
        ret['duration'] = 0
        if instance.hangup_time is not None and instance.pickup_time is not None:
          ret['duration'] = (instance.hangup_time - instance.pickup_time).total_seconds()
        
        return ret


class GamePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('number', 'name', 'score', 'answers')

    answers = PlayerAnswerSerializer(many=True, read_only=True)


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game

    players = GamePlayerSerializer(many=True, read_only=True)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'num_players', 'score_max', 'score_total', 'code', 'team', 'start_time')
    num_players = serializers.IntegerField(required=False, read_only=True)
    score_max = serializers.IntegerField(required=False, read_only=True)
    score_total = serializers.IntegerField(required=False, read_only=True)


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
