from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db

from . import schemas
from . import crud



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

@app.post("/ventas", response_model=schemas.VentaResponse)
def crear_venta(
    venta: schemas.VentaCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_venta(db, venta)

    
    