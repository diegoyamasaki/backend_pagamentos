FROM python:3.10.7

ENV APPLICATION_ROOTS=/home/app

RUN  mkdir -p $APPLICATION_ROOTS

WORKDIR $APPLICATION_ROOTS

COPY . $APPLICATION_ROOTS

RUN pip install -r requirements.txt

CMD ["make", "job"]