from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query, Depends

estudiante_router = APIRouter()

estudiantes = [
    {
        "id": 1053785856,
        "nombre": "Juan",
        "apellido": "Gonzales",
        "celular": "3156789087",
        "email": "jgon@correo.com",
        "ciudad": "Medellin",
        "pais": "Colombia"
    },
    {
        "id": 1022394743,
        "nombre": "Luisa",
        "apellido": "Perez",
        "celular": "3126765087",
        "email": "lpe@hotmail.com",
        "ciudad": "Lima",
        "pais": "Peru"
    },
    {
        "id": 1022348030,
        "nombre": "Zeref",
        "apellido": "Ger",
        "celular": "3106790026",
        "email": "zer56@outmail.com",
        "ciudad": "Buenos Aires",
        "pais": "Argentina"
    },
    {
        "id": 32743684,
        "nombre": "Felipe",
        "apellido": "Montenegro",
        "celular": "3203490166",
        "email": "mon_lo@mail.com",
        "ciudad": "Bogota",
        "pais": "Colombia"
    }
]

#Consulta para devolver la informacion de un estudiante
@estudiante_router.get("/estudiante/", tags=['estudiante'], status_code=200)
def info_estudiante(id: int):
    for est in estudiantes:
        if est["id"] == id:
            return JSONResponse(status_code=200, content={'info': est, 'message': "La información del estudiante fue encontrada exitosamente."})
    return JSONResponse(status_code=404, content={'message': "La información del estudiante no pudo ser encontrada"})