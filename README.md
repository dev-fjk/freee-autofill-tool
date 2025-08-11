# freee-autofill-tool

Freee の勤怠管理システムへの自動入力を支援するツールです。

React（フロントエンド）と FastAPI（バックエンド）で構成されています。

## 利用技術

- **Web Server**: Nginx
- **フロントエンド**: Node:22, React:18, TypeScript, Chakra UI
- **バックエンド**: FastAPI (Python 3.12.4)
- **開発ツール**: Vite, ESLint, Prettier, uv, Ruff, Docker

## 開発ツール

VSCode を利用しています。<br>
git hub copilot のコミットメッセージの自動生成設定も入れているので、copilot を vscode で入れると楽です。

## 必要な VSCode 拡張機能

- ESLint
- Prettier - Code formatter
- React Developer Tools
- Python
- Pylance
- Python Debugger
- Python Environments
- Ruff
- TOML Language Support
- auto Docstring
- GitHub Copilot
- GitHub Copilot Chat

## Frontend

### App の実行

```
# Appの実行
$ cd frontend
$ npm run dev

# ライブラリのinstall
$ npm install
```

### src/api の生成(Open API Generator)

- (1) Fast API を起動し、後述の Swagger UI から openapi.json をダウンロードします。
- (2) frontend/openapi.json を上書きします。
- (3) frontend ディレクトリで以下のコマンドを押下し、src/api 配下のソースを更新します。

```
$ openapi-generator-cli generate -i openapi.json -g typescript-axios -o src/api
```

## Backend

## FastAPI の起動/Swagger からの動作確認

前提として Python/uv の導入及び、 backend ディレクトリで uv venv を実行し仮想環境を作成すること

backend ディレクトリに移動し、以下のコマンドを実行しましょう<br>

```
$ uvicorn app.main:app --reload
```

また、.env_example をコピーし、.env を同じ階層に配置してください。

### Swagger

Fast API 起動後に以下 URL から Swagger にアクセスして動作確認ができます。

http://127.0.0.1:8000/docs

## DB の生成(Docker Compose)

事前に Docker Desktop の導入が必要です。 docker-compose.yml と同階層で操作してください。

Docker を利用できない場合自身で PostgreSQL を導入してください。

```
# DBの生成
$ docker compose up -d

# DBの削除(volume含む)
$ docker compose down -v
```
