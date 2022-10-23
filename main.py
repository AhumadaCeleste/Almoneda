import uvicorn
from fastapi import FastAPI, Form, Response
from fastapi.middleware.cors import CORSMiddleware
from model.usuarios import UsuariosImplementadoConDiccionario
from controller.login import LoginController
from controller.registro import RegistroController
from controller.reestablecer import ReestablecerController

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

db = UsuariosImplementadoConDiccionario({
    "Roberto": { "nombre": "Roberto", "apellido": "Perez", "usuario": "Roberto", "clave": "123456", "email": "roberto.carlos.alfonso@gmail.com", "nacimiento": 17/9/2000, "tipo": 3 },
    "Martin": { "nombre": "Martin", "apellido": "Rodriguez", "usuario": "Martin", "clave": "654321", "email": "martin@gmail.com", "nacimiento": 10/5/2000, "tipo": 3 },
    "Julia": { "nombre": "Julia", "apellido": "Gonzalez", "usuario": "Julia", "clave": "109283", "email": "julia@gmail.com", "nacimiento": 12/12/2000, "tipo": 3 },
    "Estela": { "nombre": "Estela", "apellido": "Flores", "usuario": "Estela", "clave": "777777", "email": "estela@gmail.com", "nacimiento": 6/6/2000, "tipo": 2 },
    "Adrian": { "nombre": "Adrian", "apellido": "Acosta", "usuario": "Adrian", "clave": "martillero", "email": "martillero@gmail.com", "nacimiento": 4/20/2000, "tipo": 1 }
})


def __cambiar_status_code(respuesta: dict[str, str], response: Response):
    if respuesta["status"] != "ok":
        response.status_code = 401


@app.post("/ingresar/", status_code=200)
def ingresar(usuario: str = Form(), clave: str = Form(), response: Response = Response()):
    controlador = LoginController(db, usuario, clave)
    return __cambiar_status_code(controlador.obtener_respuesta(), response)


@app.post("/registrar/", status_code=200)
def registrar(nombre: str = Form(), apellido: str = Form(), email: str = Form(), usuario: str = Form(), clave: str = Form(), nacimiento: str = Form(), response: Response = Response()):
    controlador = RegistroController(db, nombre, apellido, email, usuario, clave, nacimiento)
    return __cambiar_status_code(controlador.obtener_respuesta(), response)


@app.post("/reestablecer/", status_code=200)
def reestablecer(email: str = Form(), response: Response = Response()):
    controlador = ReestablecerController(db, email)
    return __cambiar_status_code(controlador.obtener_respuesta(), response)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")