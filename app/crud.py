from sqlalchemy.orm import Session
from .models import Producto
from .schemas import ProductoCreate

def crear_producto(db: Session, producto: ProductoCreate):
    nuevo_producto = Producto(
        nombre=producto.nombre,
        precio=producto.precio
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto

def obtener_productos(db: Session):
    return db.query(Producto).all()