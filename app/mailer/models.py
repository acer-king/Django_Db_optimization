# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from six import python_2_unicode_compatible
from django.db.models import Sum


class Company(models.Model):
    name = models.CharField(max_length=150)
    bic = models.CharField(max_length=150, blank=True)

    def get_order_count(self):
        result = self.orders.all().count()
        return result

    def get_order_sum(self):
        result = self.orders.all().aggregate(Sum('total'))
        return result['total__sum']

    def __str__(self):
        return "%s" % self.name


class Contact(models.Model):
    company = models.ForeignKey(
        Company, related_name="contacts", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()

    def get_order_count(self):
        result = self.orders.all().count()
        return result

    def __str__(self):
        return self.first_name+" " + self.last_name


@python_2_unicode_compatible
class Order(models.Model):
    order_number = models.CharField(max_length=150)
    company = models.ForeignKey(
        Company, related_name="orders", on_delete=models.CASCADE)
    contact = models.ForeignKey(
        Contact, related_name="orders", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=18, decimal_places=9, db_index=True)
    order_date = models.DateTimeField(null=True, blank=True)
    # for internal use only
    added_date = models.DateTimeField(auto_now_add=True)
    # for internal use only
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.order_number
