from sqlalchemy import Column, Integer, String, Date, Boolean, CheckConstraint
from app.database import Base


class Periodo(Base):
    __tablename__ = "periodos"

    id_periodo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    activo = Column(Boolean, nullable=False, default=False)

    __table_args__ = (
        CheckConstraint("fecha_fin >= fecha_inicio", name="chk_periodo_fechas"),
    )