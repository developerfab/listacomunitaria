from django.test import TestCase
from generador.models import User, Lista
from django.contrib.auth.models import User

class TestUsuario(TestCase):
    def test_adicion_de_usuario(self):
        """
        Este test se encarga de probar la adicion de un usuario al aplicativo web
        """
        user = User.objects.create_user('fab','fab7696650@hotmail.com','123')
        user.save()

        self.assertEqual(user.email,"fab7696650@hotmail.com")
    def test_ingresar_lista(self):
        """
        Esta test se encarga de probar la insercion de url en las listas de
        reproduccion de cada usuario
        """
        usuario = User()
        #import pdb; pdb.set_trace()
        usuario.nombre = "cristian"
        usuario.nick = "fab48"
        usuario.correo = "fab7696650@hotmail.com"
        usuario.password = "123456"
        usuario.save()

        lista = Lista()
        lista.url = "http://www.youtube.com"
        lista.obj_usuario = usuario
        lista.save()

        canciones = Lista.objects.filter(obj_usuario=usuario)
        self.assertEqual(canciones[0].url,"http://www.youtube.com")

