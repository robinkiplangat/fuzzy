COMPOSE = docker-compose

build:
	$(COMPOSE) build

web:
	$(COMPOSE) up web

enter:
	$(COMPOSE) exec web bash
