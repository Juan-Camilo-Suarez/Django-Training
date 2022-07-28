import time

from django.core.management import BaseCommand

from web.services import check_sites


class Command(BaseCommand):
    def add_arguments(self, parser):
        # python manage.py check_sites --daemon true
        parser.add_argument("--daemon", dest='daemon', help="Start daemon process", type=bool)

    def handle(self, daemon, *args, **options):
        while True:
            site_history = check_sites()
            print(f'{len(site_history)} sites checked')
            if not daemon:
                break
            time.sleep(60)

