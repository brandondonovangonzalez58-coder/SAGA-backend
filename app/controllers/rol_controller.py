from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import Rol


class RolController:

    @staticmethod
    def listar(db: Session):
        return db.query(Rol).all()

    @staticmethod
    def obtener(id_rol: int, db: Session):
        rol = db.query(Rol).filter(Rol.id_rol == id_rol).first()
        if not rol:
            raise HTTPException(status_code=404, detail="Rol no encontrado")
        return rol

    @staticmethod
    def crear(datos, db: Session):
        nuevo = Rol(**datos.model_dump())
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return nuevo

    @staticmethod
    def actualizar(id_rol: int, datos, db: Session):
        rol = RolController.obtener(id_rol, db)
        for campo, valor in datos.model_dump(exclude_unset=True).items():
            setattr(rol, campo, valor)
        db.commit()
        db.refresh(rol)
        return rol

    @staticmethod
    def eliminar(id_rol: int, db: Session):
        rol = RolController.obtener(id_rol, db)
        db.delete(rol)
        db.commit()
        return {"mensaje": "Rol eliminado"}