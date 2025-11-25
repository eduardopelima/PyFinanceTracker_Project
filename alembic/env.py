from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context

import pkgutil
import app.models

for module in pkgutil.iter_modules(app.models.__path__):
    __import__(f"app.models.{module.name}")


from app.database import Base, engine

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,       # detect column type changes
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
