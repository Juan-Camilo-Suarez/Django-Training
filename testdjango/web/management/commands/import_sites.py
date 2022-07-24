import sys

from django.core.management import BaseCommand

from web.models import Site


class Command(BaseCommand):
    def handle(self, *args, **options):
        fd = sys.stdin
        user_id = 10

        count = 0

        for line in fd:
            line = line.strip()
            name = line.replace('https://', '').replace('http://', '').strip('/')
            site = Site(url=line, name=name, user_id=user_id)
            site.save()
            count += 1

        print(f'{count} sites added')
