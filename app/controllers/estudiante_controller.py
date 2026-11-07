from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional
from app.models import Estudiante, Usuario, Grupo

class EstudianteController:

    @staticmethod
    def _formatear_estudiante(est: Estudiante):
        return {
            "id_estudiante": est.id_estudiante,
            "id_usuario": est.id_usuario,
            "id_grupo": est.id_grupo,
            "fecha_ingreso": est.fecha_ingreso,
            "grupo": {
                "id_grupo": est.grupo.id_grupo,
                "nombre": est.grupo.nombre,
                "turno": est.grupo.turno
            } if est.grupo else None,
            "usuario": {
                "id_usuario": est.usuario.id_usuario,
                "nombre": est.usuario.nombre,
                "apellidos": est.usuario.apellidos,
                "correo": est.usuario.correo,
                "matricula": est.usuario.matricula,
                "id_rol": est.usuario.id_rol,
                "rol": est.usuario.rol.nombre if est.usuario.rol else None,
                "activo": est.usuario.activo
            } if est.usuario else None
        }

    @staticmethod
    def listar(db: Session, buscar: Optional[str] = None):
        query = db.query(Estudiante).options(
            joinedload(Estudiante.usuario).joinedload(Usuario.rol),
            joinedload(Estudiante.grupo)
        )
        
        if buscar:
            query = query.join(Estudiante.usuario).filter(
                (Usuario.nombre.like(f"%{buscar}%")) | 
                (Usuario.apellidos.like(f"%{buscar}%")) |
                (Usuario.matricula.like(f"%{buscar}%")) |
                (Estudiante.fecha_ingreso.like(f"%{buscar}%"))
            )
                
        estudiantes = query.all()
        return [EstudianteController._formatear_estudiante(est) for est in estudiantes]

    @staticmethod
    def listar_por_grupo(id_grupo: int, db: Session):
        estudiantes = db.query(Estudiante).options(
            joinedload(Estudiante.usuario).joinedload(Usuario.rol),
            joinedload(Estudiante.grupo)
        ).filter(Estudiante.id_grupo == id_grupo).all()
        
        return [EstudianteController._formatear_estudiante(est) for est in estudiantes]

    @staticmethod
    def obtener(id_estudiante: int, db: Session):
        est = db.query(Estudiante).options(
            joinedload(Estudiante.usuario).joinedload(Usuario.rol),
            joinedload(Estudiante.grupo)
        ).filter(Estudiante.id_estudiante == id_estudiante).first()
        
        if not est:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        return EstudianteController._formatear_estudiante(est)

    @staticmethod
    def crear(datos, db: Session):
        try:
            nuevo = Estudiante(**datos.model_dump())
            db.add(nuevo)
            db.commit()
            db.refresh(nuevo)
            return EstudianteController.obtener(nuevo.id_estudiante, db)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="El ID de usuario o grupo no existe, o el alumno ya está registrado en ese grupo.")

    @staticmethod
    def actualizar(id_estudiante: int, datos, db: Session):
        est_db = db.query(Estudiante).filter(Estudiante.id_estudiante == id_estudiante).first()
        if not est_db:
             raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        try:
            for campo, valor in datos.model_dump(exclude_unset=True).items():
                setattr(est_db, campo, valor)
            db.commit()
            db.refresh(est_db)
            return EstudianteController.obtener(id_estudiante, db)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="No se pudo actualizar: Revisa que los IDs existan.")

    @staticmethod
    def eliminar(id_estudiante: int, db: Session):
        est = db.query(Estudiante).filter(Estudiante.id_estudiante == id_estudiante).first()
        if not est:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        try:
            db.delete(est)
            db.commit()
            return {"mensaje": "Estudiante eliminado correctamente"}
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="No se puede eliminar: El estudiante tiene asistencias ligadas.")