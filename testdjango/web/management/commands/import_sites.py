import sys

from django.core.management import BaseCommand

from web.models import Site


class Command(BaseCommand):
    def add_arguments(self, parser):
        # echo 'url' | python manage.py import_sites --user_id #
        parser.add_argument('--user_id', dest='user_id', help='user ID', type=int)

    def handle(self, user_id, *args, **options):
        fd = sys.stdin

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
