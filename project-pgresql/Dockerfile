FROM python:3.10-slim

WORKDIR /code

COPY ../orm-dbmigration/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../orm-dbmigration/app /code/app
COPY ../orm-dbmigration/alembic.ini /code/
COPY ../orm-dbmigration/alembic /code/alembic

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 