import uuid
from model.serialization import Serializable

class Controller:
    UUID_INVALIDO = "UUID inválido"

    def __init__(self):
        self.__respuesta = {}

    def _verificar(self, atributo: str, mensaje_de_error: str) -> bool:
        if not atributo:
            self.__respuesta = { "status": "error", "mensaje": mensaje_de_error }
            return False

        return True

    def _verificar_uuid(self, uid: str) -> bool:
        try:
            uuid.UUID(uid)
            return True
        except ValueError:
            self.__respuesta = { "status": "error", "mensaje": self.UUID_INVALIDO }
            return False

    def _responder_bien_con(self, mensaje: str) -> None:
        self.__respuesta = { "status": "ok", "mensaje": mensaje }

    def _responder_bien_incluyendo_id(self, mensaje: str, id: uuid.UUID) -> None:
        self.__respuesta = { "status": "ok", "mensaje": mensaje, "id": str(id) }

    def _responder_bien_serializando(self, model: Serializable):
        self.__respuesta = { "status": "ok", "item": model.serialize() }
        
    def _responder_bien_con_numero(self, key: str, valor: int):
        self.__respuesta = { "status": "ok", key: valor }

    def _responder_mal_con(self, mensaje: str) -> None:
        self.__respuesta = { "status": "error", "mensaje": mensaje }

    def obtener_respuesta(self) -> dict[str, str]:
        return self.__respuesta