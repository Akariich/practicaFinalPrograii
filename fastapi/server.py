import shutil

import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile,Form
import pandas as pd
from typing import  List

from pydantic import BaseModel as PydanticBaseModel
class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Videojuegos(BaseModel):
    rank: str
    name: str
    platform: str
    year: str
    genre: str
    publisher: str
    na_sales: str
    eu_sales: str
    jp_sales: str
    other_sales: str
    global_sales: str


class videojuegosventas(BaseModel):
    videojogos: List[Videojuegos]

app = FastAPI(
    title="Servidor de datos",
    description="""Servimos datos de contratos, pero podríamos hacer muchas otras cosas, la la la.""",
    version="0.1.0",
)

@app.get("/retrieve_data/")
def retrieve_data ():
    todosmisdatos = pd.read_csv('./videojuegos_ventas.csv', sep=';')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = videojuegosventas()
    listado.videojogos = todosmisdatosdict
    return listado
