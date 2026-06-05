from pydantic import BaseModel
from datetime import date

class ProductoBase(BaseModel):
    nombre: str
    precio: float

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id_producto: int

    class Config:
        from_attributes = True
        
        
class VentaBase(BaseModel):
    fecha: date
    id_usuario:int

class VentaResponse(VentaBase):
    pass

class VentaCreate(VentaBase):
    id_venta:int
    
    class Config:
        from_attributes = True


