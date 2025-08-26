
# Docker Compose Commands

## Access Terminal inside of docker-compose appliction.
-> docker-compose exec web bash
-> ls
-> python manage.py createsuperuser


## Run - Docker Compose
-> docker compose up --build
-> docker compose down


## Run - Docker Compose Prod
----------------------------
-> docker compose -f docker-compose.prod.yml up --build
-> docker compose -f docker-compose.prod.yml down

# Django Terminal:-
docker compose -f docker-compose.prod.yml exec web bash
root@75a59de2e9f4:ls
root@75a59de2e9f4:/app# python manage.py createsuperuser


# Postgres:17 - Docker Compose EXEC - cmd:-
-------------------------------------------
docker compose -f docker-compose.prod.yml exec db psql -U postgres -d djangodb

\l
\c djangodb
\dt


# Backup.
-> Create Folder - backup
docker compose -f docker-compose.prod.yml exec db pg_dump -U postgres djangodb > backup/backup_20250824.sql


## Postgresdb in Winows cmd:
----------------------------
psql -U postgres
\l
\c djangodb
\dt


# Docker Compose - Take Backup & Restore
----------------------------------------
Backup inside docker-compose:-
------------------------------
docker compose -f docker-compose.prod.yml exec db pg_dump -U postgres djangodb > backup/backup_20250824.sql

Restore in Local system:-
-------------------------
psql -U postgres -d djangodb -h localhost -p 5432 -f backup.sql


Restore in Docker Volume:-
--------------------------
docker compose exec -T db psql -U postgres -d djangodb < backup/backup_20250824.sql