#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --no-input

# Aplicar migraciones a la base de datos (Supabase)
python manage.py migrate