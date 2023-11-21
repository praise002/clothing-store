ifneq (,$(wildcard ./.env))
include .env
export 
ENV_FILE_PARAM = --env-file .env

endif

create_env:
	py -m venv my_env

act:
	source env/Scripts/activate

mmig: # run with "make mmig" or "make mmig app='app'"
	if [ -z "$(app)" ]; then \
		python manage.py makemigrations; \
	else \
		python manage.py makemigrations "$(app)"; \
	fi

mig: # run with "make mig" or "make mig app='app'"
	if [ -z "$(app)" ]; then \
		python manage.py migrate; \
	else \
		python manage.py migrate "$(app)"; \
	fi

serv:
	python manage.py runserver

suser:
	python manage.py createsuperuser

cpass:
	python manage.py changepassword

shell:
	python manage.py shell

sapp:
	python manage.py startapp

reqn:
	python -r requirements.txt

ureqn:
	python > requirements.txt

# DOCKER COMMANDS
build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

show-logs:
	docker-compose logs