FROM tiangolo/uwsgi-nginx-flask:python3.10

ENV PYTHONBUFFERED=1

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app