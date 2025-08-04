from app.models import ProjectExcelFormat
from app.schemas.project_excel_format import ProjectExcelFormatRead


def convert_excel_format_to_read_model(entity: ProjectExcelFormat) -> ProjectExcelFormatRead:
    return ProjectExcelFormatRead(
        project_id=entity.project_id,
        date_type=entity.date_type,
        start_line=entity.start_line,
        date_col=entity.date_col,
        date_format=entity.date_format,
        start_date_col=entity.start_date_col,
        end_date_col=entity.end_date_col,
        created_at=entity.created_at,
        created_by=entity.created_by,
        updated_at=entity.updated_at,
        updated_by=entity.updated_by,
    )
