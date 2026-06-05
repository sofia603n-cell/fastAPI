from sqlalchemy.orm import Session
from .models import Producto, Venta, Usuario
from .schemas import ProductoCreate, VentaCreate, UsuarioCreate

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
        fecha_venta=venta.fecha_venta,
        id_usuario=venta.id_usuario
    )
    
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    
    return nueva_venta

def obtener_ventas(db: Session):
    return db.query(Venta).all()


def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo_usuario = Usuario (
        nombre_usuario=usuario.nombre_usuario,
        apellido_usuario=usuario.apellido_usuario,
        id_rol =  usuario.id_rol,
        contraseña= usuario.contraseña
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return nuevo_usuario

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()