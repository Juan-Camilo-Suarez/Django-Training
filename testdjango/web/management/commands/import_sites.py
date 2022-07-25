import sys

from django.core.management import BaseCommand

from web.models import Site


class Command(BaseCommand):
    def handle(self, *args, **options):
        fd = sys.stdin
        user_id = 10

        count = 0
        sites = []

        for line in fd:
            line = line.strip()
            name = line.replace('https://', '').replace('http://', '').strip('/')
            site = Site(url=line, name=name, user_id=user_id)
            sites.append(site)
            count += 1

        Site.objects.bulk_create(sites)

        print(f'{count} sites added')
