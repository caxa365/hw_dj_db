import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            id = int(phone['id'])
            name = phone['name']
            image = phone['image']
            price = int(phone['price'])
            release_date = phone['release_date']
            lte_exists = bool(phone['lte_exists'])
            slug = slugify(name)

            phone = Phone(id=id, name=name, image=image, price=price, release_date=release_date, lte_exists=lte_exists, slug=slug)
            phone.save()