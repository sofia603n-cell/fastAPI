from sqlalchemy import Column, Integer, String, Numeric, Date
from .database import Base

class Producto(Base):
    __tablename__ = "producto"

    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)


class Venta(Base):
    __tablename__ = "venta"

    id_venta = Column(Integer, primary_key=True, index=True)
    fecha_venta = Column(Date, nullable=False)
    id_usuario = Column(Integer, nullable=False)
    
    
    
class Usuario(Base):
    __tablename__ = "usuario"
    
    id_usuario = Column (Integer, primary_key=True, index=True)
    nombre_usuario= Column(String, nullable=False)
    apellido_usuario=Column(String, nullable=False)
    id_rol = Column(Integer, nullable=False)
    contraseña = Column(String, nullable=False)
    
