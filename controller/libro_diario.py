from controller.controlador import Controlador
from model.database import BaseDeDatos
from services.libro_diario import ServicioLibroDiario


class ControladorLibroDiario(Controlador):
    VENTA_EXITOSA = "El lote ha sido vendido exitosamente"

    def __init__(self, db: BaseDeDatos):
        self.__db = db

    def vender(self, puja_uid: int) -> None:
        try:
            ServicioLibroDiario(self.__db).agregar(puja_uid)
            self._responder_bien_con(self.VENTA_EXITOSA)
        except Exception as err:
            self._responder_mal_con(str(err))
