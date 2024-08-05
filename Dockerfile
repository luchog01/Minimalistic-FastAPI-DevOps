# Dockerfile
FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app ./app

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]