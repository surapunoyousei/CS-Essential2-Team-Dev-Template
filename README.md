# CS Essential Team Development

このプロジェクトは東洋大学情報連携学部・情報連携基礎演習 II（コンピューターサイエンス基礎演習 II）の課題として作成したものです。

## 🛠 技術スタック

### フロントエンド

- React.js
- TypeScript
- Vite
- pnpm（パッケージマネージャー）

### バックエンド

- Django
- SQLite3

## 🚀 開発環境のセットアップ

### 前提条件

- Node.js (18.x 以上)
- Python (3.8 以上)
- pnpm
- pip

### バックエンドのセットアップ

1. Python の仮想環境を作成し、有効化します：

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

2. 必要なパッケージをインストールします：

```bash
cd backend
pip install -r requirements.txt
```

3. データベースのマイグレーションを実行します：

```bash
python manage.py migrate
```

4. 開発サーバーを起動します：

```bash
python manage.py runserver
```

### フロントエンドのセットアップ

1. 依存パッケージをインストールします：

```bash
cd frontend
pnpm install
```

2. 開発サーバーを起動します：

```bash
pnpm dev
```

## 📁 プロジェクト構造

```
.
├── frontend/        # フロントエンドのソースコード
│   ├── src/         # Reactアプリケーションのソース
│   └── public/      # 静的ファイル
│
└── backend/         # バックエンドのソースコード
    ├── api/         # APIエンドポイント
    ├── app/         # Djangoアプリケーション
    └── manage.py    # Djangoの管理スクリプト
```

## 🤝 コントリビューション

1. このリポジトリをフォークします
2. 新しいブランチを作成します (`git checkout -b feature/amazing-feature`)
3. 変更をコミットします (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュします (`git push origin feature/amazing-feature`)
5. プルリクエストを作成します
