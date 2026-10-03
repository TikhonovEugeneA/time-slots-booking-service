#!/bin/bash
set -e

poetry run alembic upgrade head

exec "$@"