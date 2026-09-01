#!/bin/bash
set -e

if []; then
    poetry run alembic init alembic
    poetry run alembic revision --autogenerate
poetry run alembic upgrade head

exec "$@"