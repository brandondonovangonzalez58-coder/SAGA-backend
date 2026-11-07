from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Usuario
from app.utils.security import hash_password

class UsuarioController:

    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Usuario)
        if buscar:
            query = query.filter(
                (Usuario.nombre.like(f"%{buscar}%")) | 
                (Usuario.apellidos.like(f"%{buscar}%")) |
                (Usuario.correo.like(f"%{buscar}%"))
            )
        return query.all()

    @staticmethod
    def obtener(id_usuario: int, db: Session):
        user = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user

    @staticmethod
    def crear(datos, db: Session):
        try:
            # Convertimos a diccionario y sacamos la contraseña plana
            user_data = datos.model_dump()
            password_plana = user_data.pop("password")
            
            # Encriptamos la contraseña y la guardamos en el campo password_hash
            user_data["password_hash"] = hash_password(password_plana)
            
            nuevo = Usuario(**user_data)
            db.add(nuevo)
            db.commit()
            db.refresh(nuevo)
            return nuevo
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="El correo o la matrícula ya están en uso.")

    @staticmethod
    def actualizar(id_usuario: int, datos, db: Session):
        user = UsuarioController.obtener(id_usuario, db)
        try:
            update_data = datos.model_dump(exclude_unset=True)
            
            # Si el usuario manda una nueva contraseña, la encriptamos
            if "password" in update_data and update_data["password"]:
                update_data["password_hash"] = hash_password(update_data.pop("password"))
            elif "password" in update_data:
                update_data.pop("password") # Si viene vacía, la ignoramos
                
            for campo, valor in update_data.items():
                setattr(user, campo, valor)
                
            db.commit()
            db.refresh(user)
            return user
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Error: Datos duplicados.")

    @staticmethod
    def eliminar(id_usuario: int, db: Session):
        user = UsuarioController.obtener(id_usuario, db)
        try:
            db.delete(user)
            db.commit()
            return {"mensaje": "Usuario eliminado"}
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="No se puede eliminar: El usuario tiene registros ligados.")