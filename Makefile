DOCKER_COMPOSE = docker-compose -f docker-compose.$(ENV).yml
APP_MANAGE_PY = run --rm api python manage.py

# build the api service
build:
	$(DOCKER_COMPOSE) build api

# make migration for new changes in the model
makemigrations:
	$(DOCKER_COMPOSE) build api
	$(DOCKER_COMPOSE) $(APP_MANAGE_PY) makemigrations

# run migration for new changes in the model
migrate:
	$(DOCKER_COMPOSE) $(APP_MANAGE_PY) migrate

# deploy the services
deploy:
	$(DOCKER_COMPOSE) build api
	$(DOCKER_COMPOSE) $(APP_MANAGE_PY) migrate
	$(DOCKER_COMPOSE) up -d
	$(DOCKER_COMPOSE) ps

# go to django shell
shell_plus:
	$(DOCKER_COMPOSE) $(APP_MANAGE_PY) shell_plus

# check for deployment issues
check:
	$(DOCKER_COMPOSE) $(APP_MANAGE_PY) check --deploy
