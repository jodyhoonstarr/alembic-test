# Alembic Test for ASRM

This repo is to test how alembic would perform on a vanilla ASRMAdmin db.

## DB Init

In order to initialize the db acquire the `adrmadmin.bak` file from the
g drive or a team member. Then initialize the database via:

```shell
LOAD_DB_BAK="true" docker-compose up --build --force-recreate --no-deps
```

## Start/Stop the DB

Once initialized the db can be started and stopped via:

```shell
# start
docker-compose up -d --build --no-deps --force-recreate
# stop
docker-compose down
# show logs
docker-compose logs -f --tail 10
```