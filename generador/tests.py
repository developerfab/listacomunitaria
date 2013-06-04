from django.test import TestCase
from generador.models import User

class TestUsuario(TestCase):
    def test_adicion_de_usuario(self):
        """
        Este test se encarga de probar la adicion de un usuario al aplicativo web
        """
        usuario = User()
        usuario.nombre = "cristian"
        usuario.nick = "fab48"
        usuario.correo = "fab7696650@hotmail.com"
        usuario.password = "123456"

        logeo = User.objects.filter(nick="fab48")
        self.assertEqual(logeo[0].password, password)
