# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
from django.shortcuts import render
from models import MacroCategory, Amount, Category


def index(request):
    logging.info('index page')
    list_macrocategory = MacroCategory.objects.all()
    list_subcategory = Category.objects.all()
    list_macrocategory_name = [model.name for model in list_macrocategory]
    list_subcategory_name = [model.category for model in list_subcategory]
    list_macrocategory_name.sort()
    logging.debug('list models created')
    context = {
        'list_macrocategory': list_macrocategory_name,
        'list_subcategory': list_subcategory_name,
        'amount': Amount.objects.first(),
        'remaining': Amount.objects.first()
    }

    return render(request, 'planning/index.html', context)
