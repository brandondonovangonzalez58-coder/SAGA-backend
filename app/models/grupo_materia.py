from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class GrupoMateria(Base):
    __tablename__ = "grupo_materias"

    id_grupo_materia = Column(Integer, primary_key=True, autoincrement=True)
    id_grupo = Column(Integer, ForeignKey("grupos.id_grupo"), nullable=False)
    id_materia = Column(Integer, ForeignKey("materias.id_materia"), nullable=False)
    # CORREGIDO: Ahora apunta a la tabla docentes
    id_docente = Column(Integer, ForeignKey("docentes.id_docente"), nullable=False)
    periodo = Column(String(30), nullable=False)
    activa = Column(Boolean, nullable=False, default=True)

    __table_args__ = (
        UniqueConstraint(
            "id_grupo", "id_materia", "id_docente", "periodo",
            name="uk_grupo_materia_docente_periodo"
        ),
    )

    # Relaciones
    grupo = relationship("Grupo", back_populates="grupos_materias")
    materia = relationship("Materia", back_populates="grupos_materias")
    # CORREGIDO: Ahora se relaciona con el modelo Docente
    docente = relationship("Docente", back_populates="materias_impartidas") 
    sesiones = relationship("Sesion", back_populates="grupo_materia")