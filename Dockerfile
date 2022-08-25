FROM python:3.10

WORKDIR /PaymentProcessor/pay

COPY PaymentProcessor/pay .

CMD [ "python3", "main.py"]
