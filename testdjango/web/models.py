from django.contrib.auth import get_user_model
from django.db import models

# para crear los usuarios de django
User = get_user_model()


class Site(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=200)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # auto_now_add=True sirve para que se crea automatico cuando se cree un modelo
    create_at = models.DateTimeField(auto_now_add=True)
    # se actualiza con la fecha del momento de la actualizacion
    update_at = models.DateTimeField(auto_now=True)

