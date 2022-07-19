from django.contrib.auth import get_user_model
from django.db import models

# para crear los usuarios de django
User = get_user_model()

class BaseModel(models.Model):
    # auto_now_add=True sirve para que se crea automatico cuando se cree un modelo
    create_at = models.DateTimeField(auto_now_add=True)
    # se actualiza con la fecha del momento de la actualizacion
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        #para que no se agrege este modelo a la base de datos
        abstract = True

#implementa BaseModel para agregar sus atributos a este modelos siendo base model
#base model clase padre
class Site(BaseModel):
    url = models.URLField()
    name = models.CharField(max_length=200)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SiteHistory(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    status_code = models.IntegerField()
    error_response_content = models.TextField(null=True, blank=True)

