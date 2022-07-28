from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager as DjangoUserManager, AbstractUser, PermissionsMixin
from django.db import models


# para crear los usuarios de django
class BaseModel(models.Model):
    # auto_now_add=True sirve para que se crea automatico cuando se cree un modelo
    create_at = models.DateTimeField(auto_now_add=True)
    # se actualiza con la fecha del momento de la actualizacion
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        # para que no se agrege este modelo a la base de datos
        abstract = True

    # para definir los metodos para crear le usuario y superusuario


class UserManager(DjangoUserManager):
    def create_user(self, username, password=None, **extra_fields):
        # en vez de username se usa email
        user = self.model(email=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        user = self.model(email=email, is_staff=True, is_superuser=True)

        user.set_password(password)
        user.save()
        return user


# implementa BaseModel para agregar sus atributos a este modelos siendo base model
# base model clase padre

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    # de esta manera se puede decir que atributo va hacer de username
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    # regula quien puede ir al admin
    is_staff = models.BooleanField(default=False)
    # update_to  para crear una carpeta ne media para guardar los avatares
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)


class Site(BaseModel):
    url = models.URLField(verbose_name="URL")
    name = models.CharField(max_length=200, verbose_name='Name')
    status = models.BooleanField(default=True, verbose_name='ready on')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')

    # mostrar el nombre de cada site
    def __str__(self):
        return self.name

    class Meta:
        # de esta manera para cada usuario se tendra un url unico
        unique_together = [('url', 'user_id')]
        # nombre del modelo en el admin
        verbose_name = 'site'
        verbose_name_plural = 'sites'


class SiteHistory(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name='site')
    status_code = models.IntegerField(null=True, verbose_name='status code')
    error_response_content = models.TextField(null=True, blank=True, verbose_name='description error')

    class Meta:
        verbose_name = 'history status site'
        verbose_name_plural = 'status histories sites'

