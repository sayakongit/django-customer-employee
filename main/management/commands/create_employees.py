import os
import random

import factory
from django.conf import settings
from django.core.management.base import BaseCommand
from factory.django import DjangoModelFactory

from main.models import Employee, Company

with open(os.path.join(settings.BASE_DIR, "main", "management", "data.txt"), "r") as file:
    text = file.read()


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    comment = text
    company = Company.objects.order_by('?').first()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Company.objects.create(name="Google")
        Company.objects.create(name="Oracle")
        Company.objects.create(name="Apple")
        Company.objects.create(name="Uber")
        Company.objects.create(name="Amazon")
        for i in range(50):
            EmployeeFactory()
            print(f"{i + 1} Users Created")
