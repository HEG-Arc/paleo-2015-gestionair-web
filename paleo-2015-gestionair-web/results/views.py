# -*- coding: UTF-8 -*-
# views.py
#
# Copyright (C) 2015 HES-SO//HEG Arc
#
# Author(s): Cédric Gaspoz <cedric.gaspoz@he-arc.ch>
#
# This file is part of paleo2015.
#
# paleo2015 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# paleo2015 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with paleo2015. If not, see <http://www.gnu.org/licenses/>.

# Stdlib imports

# Core Django imports
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Third-party app imports

# paleo2015 imports
from .models import Game


class ResultsRedirectView(RedirectView):

    permanent = True

    def get_redirect_url(self, pk):
        return reverse('results-detail-view', args=(pk,))


class ResultsDetailView(DetailView):

    model = Game

    def get_object(self, queryset=None):
        simulation = get_object_or_404(Game, pk=self.kwargs['pk'])
        return simulation