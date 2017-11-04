# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .utils import *

# Create your views here.

def resultsView(request):
    return render(request, 'main/base.html')