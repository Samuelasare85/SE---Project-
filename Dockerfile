FROM python:3.10

WORKDIR /PaymentProcessor/pay

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /pay .

CMD [ "python3", "main.py"]