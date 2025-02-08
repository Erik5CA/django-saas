from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Say hello'

    def handle(self, *args, **options):
        print('Hello World')
