run:
	uvicorn main:app --reload --host 0.0.0.0 --port 3030

run-celery:
	watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery -A speech_tasks.celery worker -l INFO