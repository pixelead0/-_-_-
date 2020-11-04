#!/bin/sh
echo "------------------------"
echo "-- POSTGRES -INI- --"
echo "------------------------"
cd /
./wait-for-it.sh db:5432 -t 0 -- echo "postgres is up"
echo "------------------------"
echo "-- POSTGRES -FIN- --"
echo "------------------------"

cd /api

echo "------------------------"
echo "-- REQUIREMENTS -INI- --"
echo "------------------------"
pip install -r requirements.txt
echo "------------------------"
echo "-- REQUIREMENTS -FIN- --"
echo "------------------------"

echo "-----------------------"
echo "-- MIGRACIONES -INI- --"
echo "-----------------------"

python manage.py migrate contenttypes
python manage.py migrate auth
python manage.py migrate users
python manage.py migrate admin
python manage.py migrate sessions

python manage.py migrate core
python manage.py migrate main

echo "-----------------------"
echo "-- MIGRACIONES -FIN- --"
echo "-----------------------"

echo "-----------------------"
echo "-- COLLECTATIC -INI- --"
echo "-----------------------"
python manage.py collectstatic --no-input
echo "-----------------------"
echo "-- COLLECTATIC -FIN- --"
echo "-----------------------"

echo "loading fixtures"
sh load_fixtures.sh

python manage.py runserver 0.0.0.0:8000
