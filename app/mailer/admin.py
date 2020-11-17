# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Contact, Company, Order


admin.site.register(Contact)
admin.site.register(Company)
admin.site.register(Order)
