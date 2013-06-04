from django.test import TestCase
from generador.models import User, Lista

class TestUsuario(TestCase):
    def test_adicion_de_usuario(self):
        """
        Este test se encarga de probar la adicion de un usuario al aplicativo web
        """
        usuario = User()
        import pdb; pdb.set_trace()
        usuario.nombre = "cristian"
        usuario.nick = "fab48"
        usuario.correo = "fab7696650@hotmail.com"
        usuario.password = "123456"
        usuario.save()

        logeo = User.objects.filter(nick="fab48")
        self.assertEqual(logeo[0].password, password)

    def test_ingresar_lista(TestCase):
        """
        Esta test se encarga de probar la insercion de url en las listas de
        reproduccion de cada usuario
        """
        lista = Lista()
        lista.url = "http://www.youtube.com"
        lista.id_usuario = "fab48"
        lista.save()

        canciones = Lista.objects.filter(id_usuario="fab48")
        self.assertEqual(canciones.url,"http://www.youtube.com")


