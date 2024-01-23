# Tokyo questions

Open http://127.0.0.1:8000/docs to see the API documentation.


## Run

Install
```shell
docker-compose up -d --wait
```

Open http://127.0.0.1:8000/docs 

### Run in development mode

```shell
docker-compose up neo4j -d --wait
```

```shell
cd service
poetry install
```

```shell
cd service
poetry run python -m service.loader
```

```shell
cd service
sh run.sh
```

Open http://127.0.0.1:8000/docs


## Stop & Clean Up

```shell
docker-compose down
```

Clean up
```shell
rm -rf ./service/venv
```

```shell
rm -rf ./data
```
