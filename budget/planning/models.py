# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Amount(models.Model):
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, default=0)
    totalVariable = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, default=total)


class MacroCategory(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    size = models.IntegerField(blank=False, null=False, default=0)
    amount = models.ForeignKey(Amount, blank=False, null=False, default=0)

    def __unicode__(self):
        return self.name

    # def set_size(self, n):
    #     self.size = n
    #     return self.size


class Category(models.Model):
    category = models.CharField(max_length=256, blank=False, null=False)
    macroCategory = models.ForeignKey(MacroCategory, blank=False, null=False)
    description = models.TextField(max_length=256, default='',blank=False, null=False)

    def __unicode__(self):
        return self.category
