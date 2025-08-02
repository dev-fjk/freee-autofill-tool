from sqlalchemy import Column, DateTime, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base

from app.config.clock import now_jst

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(255), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    start_break_time = Column(Time, nullable=False)
    end_break_time = Column(Time, nullable=False)
    update_key = Column(Integer)
    created_at = Column(DateTime, default=now_jst)
    created_by = Column(String(100))
    updated_at = Column(DateTime, default=now_jst, onupdate=now_jst)
    updated_by = Column(String(100))
