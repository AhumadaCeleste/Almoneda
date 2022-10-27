from model.subastas import Subastas
from model.usuarios import Usuarios
from model.articulos import Articulos
from model.lotes import Lotes


class BaseDeDatos:
    def __init__(self, usuarios: Usuarios, subastas: Subastas, articulos: Articulos, lotes: Lotes):
        self.__usuarios = usuarios
        self.__subastas = subastas
        self.__articulos = articulos
        self.__lotes = lotes

    @property
    def Usuarios(self) -> Usuarios:
        return self.__usuarios

    @property
    def Subastas(self) -> Subastas:
        return self.__subastas

    @property
    def Articulos(self) -> Articulos:
        return self.__articulos

    @property
    def Lotes(self) -> Lotes:
        return self.__lotes
