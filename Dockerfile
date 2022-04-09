FROM python:3.8

WORKDIR /flipkart-app

COPY ./requirements.txt /flipkart-app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /flipkart-app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

