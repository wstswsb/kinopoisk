ENV=local
include ./secrets/$(ENV)/.env
APP_NAME=kinopoisk

use_secrets:
	cp ./secrets/$(ENV)/.env ./.


down:
	docker-compose down

build: use_secrets
	docker-compose build

up: build
	docker-compose up -d

unit_tests: up
	docker-compose exec -T kinopoisk pytest -s --cov-report term-missing --cov=. ./tests/unit/

some_unit_tests: up
	docker-compose exec -T kinopoisk pytest -s --cov-report term-missing --cov=. ./tests/unit/$(TEST_PATH)

integration_tests: up
	docker exec -it kinopoisk pytest ./tests/integration

tests: up
	docker-compose exec -T kinopoisk pytest -s --cov-report term-missing --cov=. ./tests/

tag: build
	docker tag $(APP_NAME):latest $(APP_NAME):$(ENV)

logs:
	docker logs kinopoisk -f

lint:
	flake8 ./
	mypy ./
