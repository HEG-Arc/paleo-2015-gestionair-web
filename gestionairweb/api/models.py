from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField


class Event(models.Model):
    id = models.CharField(verbose_name=_("unique alphanum id"), max_length=10, blank=False, null=False, primary_key=True)
    name = models.CharField(verbose_name=_("name"), max_length=250, blank=False, null=False)
    location = models.CharField(verbose_name=_("location"), max_length=250, blank=False, null=False)
    start_date = models.DateField(verbose_name=_("start date"), null=False)
    end_date = models.DateField(verbose_name=_("end date"), null=True, blank=True)

    def __str__(self):
        return u'%s %s (%s) %s %s' % (self.name, self.location, self.id, self.start_date, self.end_date if self.end_date else '')


class Score(models.Model):
    code = models.CharField(verbose_name=_("player event code"), max_length=250, blank=False, null=False, primary_key=True)
    json = JSONField()

    def __str__(self):
        return u'%s' % self.code


class Statistic(models.Model):
    event_code = models.CharField(verbose_name=_("Event code"), max_length=10)
    event_name = models.CharField(verbose_name=_("Name of the event"), max_length=250, blank=True, null=True)
    stats_date = models.DateField(verbose_name=_("Date of the statistics"))
    creation = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    stats = JSONField()

    def __str__(self):
        return u'%s-%s-%s' % (self.event_name, stats_date, creation)

