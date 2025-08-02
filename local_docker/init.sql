-- 拡張機能: pg_trgm（あいまい検索用）
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- テーブル作成
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    project_description TEXT,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    start_break_time TIME NOT NULL,
    end_break_time TIME NOT NULL,
    update_key INT CHECK (update_key BETWEEN 0 AND 9999) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(20) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(20) NOT NULL
);

-- カラムコメントを付与
COMMENT ON COLUMN projects.project_id IS 'プロジェクトID（自動採番）';
COMMENT ON COLUMN projects.project_name IS 'プロジェクト名';
COMMENT ON COLUMN projects.project_description IS 'プロジェクトの説明';
COMMENT ON COLUMN projects.start_time IS '始業時刻';
COMMENT ON COLUMN projects.end_time IS '終業時刻';
COMMENT ON COLUMN projects.start_break_time IS '休憩開始時刻';
COMMENT ON COLUMN projects.end_break_time IS '休憩終了時刻';
COMMENT ON COLUMN projects.update_key IS '更新キー（0〜9999）';
COMMENT ON COLUMN projects.created_at IS '作成日時';
COMMENT ON COLUMN projects.created_by IS '作成者';
COMMENT ON COLUMN projects.updated_at IS '更新日時';
COMMENT ON COLUMN projects.updated_by IS '更新者';

-- プロジェクト名の部分一致検索用 GINインデックス
CREATE INDEX idx_projects_project_name_trgm 
    ON projects USING gin (project_name gin_trgm_ops);

INSERT INTO projects (
    project_name,
    project_description,
    start_time,
    end_time,
    start_break_time,
    end_break_time,
    update_key,
    created_by,
    updated_by
) VALUES
('自社勤怠表', '自社向けの勤怠表です', '10:00:00', '19:00:00', '12:00:00', '13:00:00', 1234, 'e024', 'e024'),
('R_Project_社内システム支援', 'R社内審査システム開発支援', '09:00:00', '17:30:00', '12:00:00', '13:00:00', 5678, 'e024', 'e024');    

CREATE TABLE project_excel_formats (
    project_id INT PRIMARY KEY,
    date_type SMALLINT NOT NULL,
    start_line INT NOT NULL,
    date_col VARCHAR(10) NOT NULL,
    date_format VARCHAR(20),
    start_date_col VARCHAR(10) NOT NULL,
    end_date_col VARCHAR(10) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL
);

-- カラムコメントはこうする
COMMENT ON COLUMN project_excel_formats.project_id IS 'プロジェクトID(projects.project_id)';
COMMENT ON COLUMN project_excel_formats.date_type IS '1: 日のみ, 2: 年月日';
COMMENT ON COLUMN project_excel_formats.start_line IS '開始行';
COMMENT ON COLUMN project_excel_formats.date_col IS '日付列名';
COMMENT ON COLUMN project_excel_formats.date_format IS '年月日フォーマット(yyyy-mm-dd, yyyy/mm/dd) type:2のときのみ';
COMMENT ON COLUMN project_excel_formats.start_date_col IS '開始時刻列';
COMMENT ON COLUMN project_excel_formats.end_date_col IS '終了時刻列';
COMMENT ON COLUMN project_excel_formats.created_at IS '作成日時';
COMMENT ON COLUMN project_excel_formats.created_by IS '作成者';
COMMENT ON COLUMN project_excel_formats.updated_at IS '更新日時';
COMMENT ON COLUMN project_excel_formats.updated_by IS '更新者';

INSERT INTO project_excel_formats (
    project_id,
    date_type,
    start_line,
    date_col,
    date_format,
    start_date_col,
    end_date_col,
    created_by,
    updated_by
) VALUES
(1, 1, 2, 'A', NULL, 'C', 'D', 'e024', 'e024'),
(2, 2, 8, 'B', 'yyyy/mm/dd', 'E', 'F', 'e024', 'e024');
