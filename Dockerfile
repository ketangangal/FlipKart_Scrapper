FROM python:3.9
COPY . /flipkart-app
WORKDIR /flipkart-app
RUN python --version
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e .
CMD ["python","app.py"]

