run:
	# uvicorn main:app --reload --host 0.0.0.0 --port 3030

run-celery:
	watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery -A tasks.celery worker -l INFO