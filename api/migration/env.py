import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv
from alembic import context

# Alembic Configオブジェクトの設定
config = context.config

# .env.localファイルを読み込む
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# 環境変数からデータベースURLを取得
database_url = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", database_url)

# ログ設定を読み込む
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# target_metadataをNoneに設定（モデルのメタデータを使用しない）
target_metadata = None

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
