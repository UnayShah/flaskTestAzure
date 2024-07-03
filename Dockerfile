FROM python:3.11-bookworm

ENV POSTGRES_DATABASE=wizerr-stage
ENV POSTGRES_DATABASE_HOST=wizerrai.cxmpk4bwej5d.us-west-2.rds.amazonaws.com
ENV POSTGRES_DATABASE_USER=hasura
ENV POSTGRES_DATABASE_PASSWORD=Success2023!
ENV POSTGRES_DATABASE_PORT=5432

WORKDIR /app

COPY /requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python", "./app.py" ]
