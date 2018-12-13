COMPOSE = docker-compose

build:
	$(COMPOSE) build

web:
	$(COMPOSE) up web migration

enter:
	$(COMPOSE) exec web bash

migration:
	$(COMPOSE) run web python manage.py makemigrations
	$(COMPOSE) run web python manage.py migrate
