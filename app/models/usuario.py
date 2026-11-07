from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, func
)
from sqlalchemy.orm import relationship
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_rol = Column(Integer, ForeignKey("roles.id_rol"), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    matricula = Column(String(30), unique=True, nullable=True)
    password_hash = Column(String(255), nullable=False)
    activo = Column(Boolean, nullable=False, default=True)
    fecha_creacion = Column(TIMESTAMP, server_default=func.now())

    # Relaciones (AQUÍ YA NO VA 'materias_impartidas')
    rol = relationship("Rol", back_populates="usuarios")
    estudiante = relationship("Estudiante", back_populates="usuario", uselist=False)
    docente = relationship("Docente", back_populates="usuario", uselist=False) 
    asistencias_registradas = relationship("Asistencia", back_populates="registrador")