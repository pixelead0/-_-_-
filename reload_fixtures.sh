docker-compose exec api rm -f /its-migrated.txt
docker-compose exec api sh load_fixtures.sh
