from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id_estudiante = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), unique=True, nullable=False)
    id_grupo = Column(Integer, ForeignKey("grupos.id_grupo"), nullable=False)
    fecha_ingreso = Column(Date)

    # Relación con Usuario (1 a 1)
    usuario = relationship("Usuario", back_populates="estudiante", uselist=False)
    
    # Relación con Grupo
    grupo = relationship("Grupo", back_populates="estudiantes")
    
    # Relación con Asistencia (en cascada para que no truene al borrar)
    asistencias = relationship("Asistencia", back_populates="estudiante", cascade="all, delete-orphan")