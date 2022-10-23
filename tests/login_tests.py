import unittest
from ddt import ddt, data, unpack
from controller.login import LoginController
from model.tipo_usuario import TipoDeUsuario
from model.usuarios import UsuariosImplementadoConDiccionario

@ddt
class LoginControllerTests(unittest.TestCase):
    __db_con_usuario = UsuariosImplementadoConDiccionario({
        "Roberto": {
            "nombre": "Roberto",
            "apellido": "Perez",
            "email": "roberto@gmail.com",
            "usuario": "Roberto",
            "clave": "123456",
            "nacimiento": 9/17/2000,
            "tipo": TipoDeUsuario.Pujador.value
        }
    })


    def test_retornar_ok_cuando_usuario_y_clave_son_correctos(self):
        sut = LoginController(self.__db_con_usuario, "Roberto", "123456")
        respuesta = sut.obtener_respuesta()
        self.assertEqual("ok", respuesta["status"])
        self.assertIn("Roberto", respuesta["mensaje"])


    @data(
        ("Roberto", "123"),
        ("Carlos", "123456")
    )
    @unpack
    def test_retornar_error_cuando_usuario_o_clave_incorrecta(self, usuario: str, clave: str):
        sut = LoginController(self.__db_con_usuario, usuario, clave)
        respuesta = sut.obtener_respuesta()
        self.assertEqual("error", respuesta["status"])
        self.assertEqual("Usuario o contraseña inválida", respuesta["mensaje"])


    def test_retornar_error_cuando_base_esta_vacia(self):
        sut = LoginController(UsuariosImplementadoConDiccionario({}), "Roberto", "123456")
        respuesta = sut.obtener_respuesta()
        self.assertEqual("error", respuesta["status"])
        self.assertEqual("Usuario o contraseña inválida", respuesta["mensaje"])


    @data(
        ("", "123456"),
        (None, "123456"),
        ("Roberto", ""),
        ("Roberto", None)
    )
    @unpack
    def test_retornar_error_cuando_falta_dato(self, usuario: str, clave: str):
        sut = LoginController(UsuariosImplementadoConDiccionario({}), usuario, clave)
        respuesta = sut.obtener_respuesta()
        self.assertEqual("error", respuesta["status"])
        self.assertIn("No se puede ingresar sin", respuesta["mensaje"])


if __name__ == "__main__":
    unittest.main()