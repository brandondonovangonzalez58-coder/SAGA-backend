from sqlalchemy import (
    Column, Integer, String, Enum, ForeignKey, TIMESTAMP, UniqueConstraint, func
)
from sqlalchemy.orm import relationship
from app.database import Base


class Asistencia(Base):
    __tablename__ = "asistencias"

    id_asistencia = Column(Integer, primary_key=True, autoincrement=True)
    id_sesion = Column(Integer, ForeignKey("sesiones.id_sesion"), nullable=False)
    id_estudiante = Column(
        Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False
    )
    estado = Column(
        Enum("Presente", "Retardo", "Falta", "Justificada"),
        nullable=False,
        default="Falta"
    )
    observaciones = Column(String(250))
    registrado_por = Column(
        Integer, ForeignKey("usuarios.id_usuario"), nullable=False
    )
    fecha_registro = Column(TIMESTAMP, server_default=func.now())

    __table_args__ = (
        UniqueConstraint(
            "id_sesion", "id_estudiante",
            name="uk_asistencia_sesion_estudiante"
        ),
    )

    sesion = relationship("Sesion", back_populates="asistencias")
    estudiante = relationship("Estudiante", back_populates="asistencias")
    registrador = relationship("Usuario", back_populates="asistencias_registradas")