from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Materia(Base):
    __tablename__ = "materias"

    id_materia = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(120), nullable=False)
    clave = Column(String(30), unique=True)
    activa = Column(Boolean, nullable=False, default=True)

    grupos_materias = relationship("GrupoMateria", back_populates="materia")