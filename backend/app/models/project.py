from sqlalchemy import CheckConstraint, Column, DateTime, Integer, String, Text, Time
from sqlalchemy.ext.declarative import declarative_base

from app.config.clock import now_jst

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(255), nullable=False)
    project_description = Column(Text)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    start_break_time = Column(Time, nullable=False)
    end_break_time = Column(Time, nullable=False)
    update_key = Column(Integer, CheckConstraint('update_key BETWEEN 0 AND 9999'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=now_jst)
    created_by = Column(String(20), nullable=False)
    updated_at = Column(DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    updated_by = Column(String(20), nullable=False)
