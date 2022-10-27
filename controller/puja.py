from controller.controller import Controller
from model.database import BaseDeDatos


class PujaController(Controller):
    PUJAR_SIN_LOTE = "No se puede pujar sin lote"
    PUJAR_SIN_PUJADOR = "No se puede pujar sin un pujador"
    LOTE_INEXISTENTE = "No se puede pujar por un lote inexistente"
    PUJADOR_INEXISTENTE = "No se puede pujar con un pujador inexistente"
    PUJA_BAJA = "No se puede pujar por menos de la última puja"

    def __init__(self, db: BaseDeDatos):
        self.__db = db

    def agregar(self, lote_uid: int, pujador_uid: int, monto: int) -> None:
        if not self._verificar(lote_uid, self.PUJAR_SIN_LOTE):
            return

        if not self._verificar(pujador_uid, self.PUJAR_SIN_PUJADOR):
            return

        lote = self.__db.Lotes.buscar_por_uid(lote_uid)
        if not self._verificar(lote, self.LOTE_INEXISTENTE):
            return

        pujador = self.__db.Usuarios.buscar_pujador_por_uid(pujador_uid)
        if not self._verificar(pujador, self.PUJADOR_INEXISTENTE):
            return

        puja = self.__db.Pujas.buscar_ultima_puja(lote)
        if puja and puja.obtener_monto() >= monto:
            self._responder_mal_con(self.PUJA_BAJA)
            return

        self.__db.Pujas.agregar(monto, pujador, lote)
        self._responder_bien_con("Puja realizada con éxito")