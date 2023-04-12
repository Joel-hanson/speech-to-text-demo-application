run-frontend:
	cd frontend && npm install && npm run build && npm run dev

run:
	python3 manage.py runserver 0.0.0.0:8000

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

shell:
	python3 manage.py shell

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

start-s2t-upload-event-source-connector:
	curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" connect:8083/connectors/ -d @connect/s2t-upload-event-source-connector.json

# start-s2t-http-sink-connector:
# 	curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" connect:8083/connectors/ -d @connect/s2t-http-sink-connector.json
# Path: Makefile