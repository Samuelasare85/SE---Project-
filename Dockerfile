FROM python:3.10

WORKDIR /PaymentProcessor/pay

COPY /pay .

CMD [ "python3", "main.py"]
