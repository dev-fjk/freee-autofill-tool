# Copilot Instructions for freee-autofill-tool

## 概要

freee-autofill-tool は、React（フロントエンド）と FastAPI（バックエンド）で構成された勤怠自動入力支援ツールです。主要な開発・運用は VSCode 上で行われます。

## アーキテクチャ

- **frontend/**: React + TypeScript。API クライアントは OpenAPI Generator で自動生成（`src/api`）。
- **backend/**: FastAPI（Python 3.12.4）。
  - `app/main.py`: エントリーポイント。CORS/認証/リクエスト ID 等のミドルウェアを設定。
  - `app/api/`: ルーター分割（例: `projects.py`, `login.py`）。
  - `app/models/`: SQLAlchemy ORM モデル（`entity.py`）。
  - `app/schemas/`: Pydantic スキーマ。
  - `app/services/`: ビジネスロジック層。
  - `app/db/`: DB セッション管理・依存関数。
  - `app/config/`: 設定・ロギング・contextvars 管理。
- **DB**: PostgreSQL（Docker Compose で起動）。
- **ログ**: `logs/` ディレクトリに JSON 形式で出力。リクエスト ID/employee_id/role 等を contextvars で付与。

## 開発・ビルド・テスト

- **フロントエンド起動**: `cd frontend && npm run dev`
- **バックエンド起動**: `cd backend && uvicorn app.main:app --reload`
- **DB 起動**: `docker compose up -d`
- **API クライアント生成**: `openapi-generator-cli generate -i openapi.json -g typescript-axios -o src/api`
- **.env 管理**: `backend/.env_example` をコピーして `.env` を作成

## コーディング規約・パターン

- **API ルーター分割**: `app/api/` 配下で機能ごとに分割し、`main.py`で`include_router`。
- **依存関数**: 共通ヘッダー（X-Employee-Id 等）は`app/api/deps.py`で定義し、`dependencies`でルーター単位適用。
- **contextvars**: employee_id, request_id, role 等は`app/config/context.py`で管理し、ミドルウェアでセット。
- **ロギング**: `app/config/logging.py`で JSON ログ。contextvars の値を自動付与。
- **DB セッション**: `app/db/session.py`の`SessionLocal`を依存関数経由で利用。
- **スキーマ**: Pydantic モデルは`schemas/`で用途ごとに分割（Read/Create/Update 等）。
- **テスト**: pytest 等で API/サービス層をテスト（tests/ディレクトリは未実装の場合あり）。

## プロジェクト固有の注意点

- **コミットメッセージ**: Copilot Chat の指示で日本語+prefix 必須（VSCode 設定参照）。
- **OpenAPI/Swagger**: API 仕様変更時は`frontend/openapi.json`を更新し、クライアント再生成。
- **DB スキーマ**: `init.sql`で DDL 管理。モデル・スキーマと整合性を保つこと。
- **ログ**: すべての API リクエストに request_id/employee_id/role を付与する設計。

## 参考ファイル

- `README.md`: 開発手順・ツール・起動方法
- `app/main.py`: サーバー起動・ミドルウェア・ルーター登録
- `app/api/projects.py`: 主要 API 実装例
- `app/config/context.py`, `app/config/logging.py`: contextvars/ロギング実装
- `app/models/entity.py`, `app/schemas/project.py`: DB/スキーマ定義

---

不明点やプロジェクト特有の例外があれば、README や各ディレクトリの実装例を参照してください。
