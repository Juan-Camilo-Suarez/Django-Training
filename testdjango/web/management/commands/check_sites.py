from django.core.management import BaseCommand

from web.services import check_sites


class Command(BaseCommand):
    def handle(self, *args, **options):
        site_history = check_sites()
        print(f'{len(site_history)} sites checked')
