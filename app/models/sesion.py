from sqlalchemy import (
    Column, Integer, Date, Time, String, Enum, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from app.database import Base


class Sesion(Base):
    __tablename__ = "sesiones"

    id_sesion = Column(Integer, primary_key=True, autoincrement=True)
    id_grupo_materia = Column(
        Integer, ForeignKey("grupo_materias.id_grupo_materia"), nullable=False
    )
    fecha = Column(Date, nullable=False)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    tema = Column(String(200))
    estado = Column(
        Enum("Abierta", "Cerrada", "Cancelada"),
        nullable=False,
        default="Abierta"
    )

    __table_args__ = (
        UniqueConstraint(
            "id_grupo_materia", "fecha", "hora_inicio",
            name="uk_sesion_gm_fecha_hora"
        ),
    )

    grupo_materia = relationship("GrupoMateria", back_populates="sesiones")
    asistencias = relationship("Asistencia", back_populates="sesion")