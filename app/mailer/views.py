# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView

from mailer.models import Company, Order, Contact
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Prefetch


class IndexView(ListView):

    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100

    def get_queryset(self):
        return super().get_queryset().prefetch_related('contacts__orders')
