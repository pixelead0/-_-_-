# This script create a new fixtures for django

echo [$(date +"%Y-%m-%d %T")] --Started--

mkdir -p api/app/users/fixtures/

# Auth
echo [$(date +"%Y-%m-%d %T")] creating fixtures from -auth.user-
docker-compose exec api python manage.py dumpdata auth.user --indent=2 >api/app/users/fixtures/user.json

echo [$(date +"%Y-%m-%d %T")] --Finished--
