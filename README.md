# freee-autofill-tool

Freee の勤怠自動入力ツールです

Render を利用して公開予定

## 利用技術

- API(backend)
  - Python:3.12.4
  - FastAPI
  - uv
  - uvicorn
  - ruff

## FastAPI の起動/Swagger からの動作確認

前提として Python/uv の導入及び、 backend ディレクトリで uv venv を実行し仮想環境を作成すること

backend ディレクトリに移動し、以下のコマンドを実行しましょう<br>

```
$ uvicorn app.main:app --reload
```

### Swagger

Fast API 起動後に以下 URL から Swagger にアクセスして動作確認ができます。

http://127.0.0.1:8000/docs

## 開発ツール
VSCodeを利用しています。<br>
git hub copilotのコミットメッセージの自動生成設定も入れているので、copilotをvscodeで入れると楽です。
