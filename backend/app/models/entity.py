from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer, SmallInteger, String, Text, Time
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

class ProjectExcelFormat(Base):
    __tablename__ = "project_excel_formats"

    project_id = Column(Integer, primary_key=True)
    date_type = Column(SmallInteger, nullable=False)
    start_line = Column(Integer, nullable=False)
    date_col = Column(String(10), nullable=False)
    date_format = Column(String(20), nullable=True)
    start_date_col = Column(String(10), nullable=False)
    end_date_col = Column(String(10), nullable=False)
    is_tested = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=now_jst)
    created_by = Column(String(100), nullable=False)
    updated_at = Column(DateTime, nullable=False, default=now_jst, onupdate=now_jst)
    updated_by = Column(String(100), nullable=False)
