from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db

from . import schemas
from . import crud



# Nicolas
from pydantic import BaseModel
from datetime import date

app = FastAPI()


@app.get("/")
def read_root():
    return {"Mensaje": "Hola Mundo"}

@app.post("/productos", response_model=schemas.ProductoResponse)
def crear_producto(
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_producto(db, producto)


#Nicolas
class Venta(BaseModel):
    fecha_venta: date
    id_usuario: int


@app.post("/ventas")
def crear_venta(venta: Venta):
    return {
        "mensaje": "Venta registrada correctamente",
        "fecha_venta": venta.fecha_venta,
        "id_usuario": venta.id_usuario
    }
    
    