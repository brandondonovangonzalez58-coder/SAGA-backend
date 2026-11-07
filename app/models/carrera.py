from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Carrera(Base):
    __tablename__ = "carreras"

    id_carrera = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(120), nullable=False, unique=True)
    siglas = Column(String(20))
    activa = Column(Boolean, nullable=False, default=True)

    grupos = relationship("Grupo", back_populates="carrera")