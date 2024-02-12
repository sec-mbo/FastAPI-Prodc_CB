from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query, Depends

modulo_router = APIRouter()

modulos = [
    {
        "curso": "SEG_GENERALES_DIAN",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    },
    {
        "curso": "EXCEL_AVANZADO_G1",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    },
    {
        "curso": "ANALISIS_FINANCIERO_MUNDIAL",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    },
    {
        "curso": "NIVELACION",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    },
    {
        "curso": "ACT_CIRCULAR_050_GENERALES_VIDA",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    },
    {
        "curso": "EVENTO_SEG_BOLIVAR",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    },
    {
        "curso": "EVENTO_SEG_BOLIVAR_2",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    },
    {
        "curso": "EVENTO_SEG_BOLIVAR_2",
        "modulo_1": "Examen 1",
        "modulo_2": "Examen 2",
        "modulo_3": "Examen 3"
    }
]

@modulo_router.get("/modulo/", tags=['modulos'], status_code=200)
def modulos_curso(curso: str):
    for modu in modulos:
        if modu["curso"] == curso:
            return JSONResponse(status_code=200, content={'modulos': modu, 'message': "Los modulos del curso han sido encontrados."})
    return JSONResponse(status_code=404, content={'message': "No existen modulos para el curso consultado"})