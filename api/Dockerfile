FROM python:3.10

WORKDIR /api

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

RUN pip install --upgrade pip

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./server /api/server

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "80"]