import unittest
from ddt import ddt, data, unpack
from controller.login import LoginController
from model.usuarios import UsuariosImplementadoConDiccionario

@ddt
class LoginControllerTests(unittest.TestCase):
    __db_con_usuario = UsuariosImplementadoConDiccionario({
        "Roberto": { "clave": "123456" }
    })


    def test_retornar_ok_cuando_usuario_y_clave_son_correctos(self):
        respuesta = LoginController(self.__db_con_usuario, "Roberto", "123456").obtener_respuesta()
        self.assertEqual("ok", respuesta["status"])
        self.assertIn("Roberto", respuesta["mensaje"])


    @data(("Roberto", "123"),
          ("Carlos", "123456"))
    @unpack
    def test_retornar_error_cuando_usuario_o_clave_incorrecta(self, usuario: str, clave: str):
        respuesta = LoginController(self.__db_con_usuario, usuario, clave).obtener_respuesta()
        self.assertEqual("error", respuesta["status"])
        self.assertEqual("Usuario o contraseña inválida", respuesta["mensaje"])


    def test_retornar_error_cuando_base_esta_vacia(self):
        respuesta = LoginController(UsuariosImplementadoConDiccionario({}), "Roberto", "123456").obtener_respuesta()
        self.assertEqual("error", respuesta["status"])
        self.assertEqual("Usuario o contraseña inválida", respuesta["mensaje"])


if __name__ == "__main__":
    unittest.main()