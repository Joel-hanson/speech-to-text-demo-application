run-frontend-install: 
	cd frontend && npm install

run-frontend-build:
	cd frontend && npm run build

run-frontend: run-frontend-install run-frontend-build
	cd frontend && npm run dev

run:
	python3 manage.py runserver 0.0.0.0:8000

run-celery:
	python3 manage.py celery

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

shell:
	python3 manage.py shell

celery-debug:
	celery call backend.celery.debug_task

celery-get-registered-tasks:
	celery inspect registered

test:
	python3 manage.py test

superuser:
	python3 manage.py createsuperuser

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

reset:
	make clean
	rm -rf db.sqlite3
	make migrate
	make superuser
	make test
