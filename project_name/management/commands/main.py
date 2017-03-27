from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<some arg>'
    help = 'Sample main '

    def handle(self, *args, **options):
        pass