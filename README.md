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

## Create an empty DB

The loader scripts above will create a populated `ASRMAdmin` db.
Use your tool of choice to generate an `EmptyASRMAdmin` db in the same cluster.

## Configure the connections

The `basemodel.py` will contain a reflected/automapped base class. 
This will read all the data it can from the connection string and use it to generate
SQLAlchemy models. Make sure `alembic/env.py` uses `target_metadata = Base.metadata` 
that references this reflected/automapped base.

Once that's done the `alembic.ini` should contain the SQLAlchemy URL but should point
to the `EmptyASRMAdmin` db.

## Generate the migrations

At this point running `alembic revision --autogenerate` will generate a single migration.
It takes the connection to the `ASRMAdmin` db and generates the SQLAlchemy to make the `EmptyASRMAdmin` db
schema match. Cleanup as needed.