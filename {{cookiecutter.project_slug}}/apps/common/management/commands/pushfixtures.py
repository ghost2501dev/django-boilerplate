from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        for fixture in settings.FIXTURES:
            call_command('loaddata', fixture)
