# docker-flask-postgresql
Flask and PostgreSQL application, dockerized. The general architecture of this template is based on https://github.com/miguelgrinberg/microblog.

### Setup
1. If needed, [install docker](https://docs.docker.com/install/) on your computer
1. Clone this repository with `git clone --recursive` to include the submodules
1. (Optional) Change the name of the databases defined in the `POSTGRES_MULTIPLE_DATABASES` variable in `docker-compose.yml`
1. Copy `src/.env.template` to `src/.env` and update as necessary

### Run
```
$ bin/build.sh
$ bin/start.sh
$ docker exec -it <web_container_name> bash
> flask init tables
> flask init user
```

### Verify
The `0.0.0.0:5000/api` endpoint should now be available

### Tests
```
$ docker exec -it <web_container_name> bash
> python -m pytest
```
