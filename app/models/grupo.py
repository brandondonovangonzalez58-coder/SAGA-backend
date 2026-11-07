from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Grupo(Base):
    __tablename__ = "grupos"

    id_grupo = Column(Integer, primary_key=True, autoincrement=True)
    id_carrera = Column(Integer, ForeignKey("carreras.id_carrera"), nullable=False)
    nombre = Column(String(50), nullable=False)
    cuatrimestre = Column(Integer)
    turno = Column(Enum("Matutino", "Vespertino", "Mixto"))
    activo = Column(Boolean, nullable=False, default=True)

    carrera = relationship("Carrera", back_populates="grupos")
    estudiantes = relationship("Estudiante", back_populates="grupo")
    grupos_materias = relationship("GrupoMateria", back_populates="grupo")