#docker run -it -p 8000:8000 app

FROM python:3.9-buster

WORKDIR /var/app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000


COPY . .


CMD uvicorn view:app --host=0.0.0.0 --port 8000
