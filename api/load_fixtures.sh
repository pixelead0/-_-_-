#!/bin/sh
FILE="/its-migrated.txt"
if ! [ -f "$FILE" ]; then
    echo "-----------------------------------"
    echo "-- INSTALACIÓN DE FIXTURES -INI- --"
    echo "-----------------------------------"

    cd /api

    echo [$(date +"%Y-%m-%d %T")] Creating fixtures -users.user-
    python manage.py loaddata app/users/fixtures/user.json

    touch $FILE
    echo "-----------------------------------"
    echo "-- INSTALACIÓN DE FIXTURES -FIN- --"
    echo "-----------------------------------"
else
    echo "--------------------------------------------"
    echo "-- Se han creado previamente los fixtures --"
    echo "--------------------------------------------"
fi

echo "-----------------------------------"
echo "-- Back   : http://0.0.0.0:8000/v1/ "
echo "-----------------------------------"
