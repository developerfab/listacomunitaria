from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=30)
    nick = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

class Lista(models.Model):
    obj_usuario = models.ForeignKey(User)
    url = models.CharField(max_length=100)

