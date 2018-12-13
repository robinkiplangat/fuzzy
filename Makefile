COMPOSE = docker-compose

build:
	$(COMPOSE) build

web:
	$(COMPOSE) up web

enter:
	$(COMPOSE) exec web bash
	
migrate:
	$(COMPOSE) exec web python manage.py makemigrations
	$(COMPOSE) exec web python manage.py migrate
