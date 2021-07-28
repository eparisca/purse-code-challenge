# purse-code-challenge
Purse Coding Challenge

## Dependencies
* [Docker Desktop](https://www.docker.com/products/docker-desktop) 

## Build

```shell
app_version="1.0.0"
./run_tests.sh
./docker_build.sh ${app_version}
./docker_build_db.sh 1.0.0
```

## Run locally
```shell
docker-compose -f docker-compose.yml up -d
open "http://localhost:5000"
```

```shell
curl -v http://localhost:5000//api/1.0/orders/232-9384712-9823512
```

## troubleshooting

```shell
docker-compose exec purse-db bash 
```
```shell
bash-5.1# psql -U dbuser purse
psql (13.3)
Type "help" for help.

purse=# select * from orders;
 order | delivery 
-------+----------
(0 rows)

purse=# \q
bash-5.1# exit
exit
```