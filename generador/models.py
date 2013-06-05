from django.db import models
from django.contrib.auth.models import User

class Lista(models.Model):
    obj_usuario = models.ForeignKey(User)
    url = models.CharField(max_length=100)

