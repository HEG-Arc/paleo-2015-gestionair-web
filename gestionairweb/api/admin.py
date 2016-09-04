from django.contrib import admin
from .models import Event, Score, Statistic


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    pass
