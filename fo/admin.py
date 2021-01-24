# -*- coding: utf-8 -*-
from django.contrib import admin

from . models import Arena, User


admin.site.register([
    Arena,
    User
])
