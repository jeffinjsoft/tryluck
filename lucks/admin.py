# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Luck)
admin.site.register(models.Like)
admin.site.register(models.Search)
admin.site.register(models.Comment)
