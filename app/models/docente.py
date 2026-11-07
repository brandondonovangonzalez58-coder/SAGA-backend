from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Docente(Base):
    __tablename__ = "docentes"

    id_docente = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), unique=True, nullable=False)
    numero_empleado = Column(String(20), unique=True, nullable=False)
    especialidad = Column(String(100), nullable=True)

    usuario = relationship("Usuario", back_populates="docente")
    materias_impartidas = relationship("GrupoMateria", back_populates="docente")