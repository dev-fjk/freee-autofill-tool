CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    start_break_time TIME NOT NULL,
    end_break_time TIME NOT NULL,
    update_key INT CHECK (update_key BETWEEN 0 AND 9999) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL
);

CREATE INDEX idx_projects_project_name_trgm ON projects USING gin (project_name gin_trgm_ops);

INSERT INTO projects (
    project_name, start_time, end_time, start_break_time, end_break_time,
    update_key, created_by, updated_by
) VALUES
('自社勤怠表', '10:00:00', '19:00:00', '12:00:00', '13:00:00', 1234, 'admin', 'admin'),
('R_Project', '09:00:00', '17:30:00', '12:00:00', '13:00:00', 5678, 'admin', 'admin');

CREATE TABLE project_excel_formats (
    project_id INT PRIMARY KEY,
    start_line INT NOT NULL,
    month_col INT NOT NULL,
    date_col INT NOT NULL,
    start_date_col INT NOT NULL,
    end_date_col INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL
);

INSERT INTO project_excel_formats (
    project_id,
    start_line,
    month_col,
    date_col,
    start_date_col,
    end_date_col,
    created_by,
    updated_by
) VALUES
(1, 2, 1, 2, 3, 4, 'admin', 'admin'),
(2, 3, 1, 2, 4, 5, 'admin', 'admin');

