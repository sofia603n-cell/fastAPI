from sqlalchemy.orm import Session
from .models import Producto, Venta
from .schemas import ProductoCreate, VentaCreate

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


def crear_venta(db: Session, venta: VentaCreate):
    nueva_venta = Venta(
        fecha=venta.fecha,
        id_usuario=venta.id_usuario
    )
    
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    
    return nueva_venta

def obtener_ventas(db: Session):
    return db.query(Venta).all()