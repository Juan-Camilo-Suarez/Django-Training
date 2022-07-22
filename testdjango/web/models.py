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

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        user = self.model(email=username, is_staff=True, is_superuser=True)
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


class Site(BaseModel):
    url = models.URLField()
    name = models.CharField(max_length=200)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SiteHistory(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    status_code = models.IntegerField()
    error_response_content = models.TextField(null=True, blank=True)
