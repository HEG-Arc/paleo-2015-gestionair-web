# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.IntegerField(help_text='The sequence of the questions for a player', verbose_name='question sequence')),
                ('answer', models.IntegerField(help_text='The answer key that was pressed during the game', verbose_name='answer given')),
                ('pickup_time', models.DateTimeField(help_text='The pick up time of the call', verbose_name='pick up time')),
                ('hangup_time', models.DateTimeField(help_text='The hang up time of the call', verbose_name='hang up time')),
                ('correct', models.IntegerField(help_text='This indicates if the answer is correct (1), false (0) or if there is no answer (NULL)', null=True, verbose_name='correct answer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('number', models.IntegerField(help_text='The number of the department', unique=True, serialize=False, verbose_name='department number', primary_key=True)),
                ('name', models.CharField(help_text='The name of the department', max_length=50, verbose_name='department')),
                ('description', models.TextField(help_text='The description of the department', verbose_name='description')),
                ('audio_file', models.FileField(help_text="The MP3 file of the department's description", upload_to=b'departments', verbose_name='audio file')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('code', models.CharField(primary_key=True, serialize=False, max_length=15, help_text='The identification code of the game', unique=True, verbose_name='code')),
                ('team', models.CharField(help_text='The name of the team (this field is not unique!)', max_length=100, verbose_name='team')),
                ('start_time', models.DateTimeField(help_text='The start time of the game', verbose_name='start time')),
                ('end_time', models.DateTimeField(help_text='The end time of the game', verbose_name='end time')),
                ('canceled', models.BooleanField(default=False, help_text='A game is canceled in the case of a no-show (time slot + grace period', verbose_name='canceled')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(primary_key=True, serialize=False, max_length=2, help_text='The ISO 3166-1 code of the language', unique=True, verbose_name='language code')),
                ('language', models.CharField(help_text='The french name of the language', max_length=100, verbose_name='language name')),
                ('flag', models.ImageField(help_text='The flag file of the language', upload_to=b'flags', verbose_name='flag file')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('number', models.IntegerField(help_text='The call number of the phone', serialize=False, verbose_name='phone number', primary_key=True)),
                ('position_x', models.FloatField(help_text='The position on the horizontal axis', null=True, verbose_name='x position', blank=True)),
                ('position_y', models.FloatField(help_text='The position on the vertical axis', null=True, verbose_name='y position', blank=True)),
                ('orientation', models.IntegerField(default=0, help_text='The orientation of the phone in degrees', verbose_name='orientation', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(help_text='The identification number of the player', verbose_name="player's number")),
                ('name', models.CharField(help_text='The name of the player', max_length=100, verbose_name="player's name")),
                ('game', models.ForeignKey(related_name='players', verbose_name='game', to='results.Game', help_text='The game in which the player takes part')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('number', models.IntegerField(help_text='The number of the question', unique=True, serialize=False, verbose_name='question number', primary_key=True)),
                ('department', models.ForeignKey(related_name='questions', verbose_name='department', to='results.Department', help_text='The department concerned by the question (aka right answer)')),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(help_text='The translated text of the question', null=True, verbose_name='translated question', blank=True)),
                ('audio_file', models.FileField(help_text='The MP3 file of the question', upload_to=b'questions', verbose_name='audio file')),
                ('language', models.ForeignKey(related_name='questions', verbose_name='language', to='results.Language', help_text='The language of the translation')),
                ('question', models.ForeignKey(related_name='translations', verbose_name='question', to='results.Question', help_text='The translated question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='phone',
            field=models.ForeignKey(related_name='answers', verbose_name='phone', to='results.Phone', help_text='The identifier of the phone used for this answer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='player',
            field=models.ForeignKey(related_name='answers', verbose_name='player', to='results.Player', help_text='The player who answered the question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', verbose_name='question', to='results.Translation', help_text='The question/language which was answered'),
        ),
    ]
