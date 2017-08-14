# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
from django.shortcuts import render
from models import MacroCategory,Amount


def index(request):
    logging.info('index page')
    list_models = MacroCategory.objects.all()
    list_models_name = [model.name for model in list_models]
    list_models_name.sort()
    logging.debug('list models created')
    context = {
        'macrocategory': list_models_name,
        'amount': Amount.objects.first(),
        'remaining': Amount.objects.first()
    }


    return render(request, 'planning/index.html', context)
