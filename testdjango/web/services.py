from urllib import response

import requests as requests

from .models import User, Site, SiteHistory


def register_user(email: str, password: str, avatar) -> User:
    user = User(email=email, avatar=avatar)
    user.set_password(password)
    user.save()
    return user


def check_sites():
    sites = Site.objects.all()
    history_objects = []
    site_objects = []

    for site in sites:
        status_code = None

        try:
            response = requests.get(site.url, timeout=10)
            status_code = response.status_code
            error_response_content = response.text if not response.ok else None
        except requests.exceptions.ConnectionError as exc:
            error_response_content = str(exc)

        history = SiteHistory(
            site=site,
            status_code=status_code,
            error_response_content=error_response_content
        )

        if status_code is not None and status_code >= 200 and status_code < 300:
            site.status = True
        else:
            site.status = False

        site_objects.append(site)
        history_objects.append(history)

    SiteHistory.objects.bulk_create(history_objects)
    Site.objects.bulk_update(site_objects, ['status'])

    return history_objects
