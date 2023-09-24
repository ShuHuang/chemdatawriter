FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3.8 python3.8-dev

RUN apt-get install -y python3-pip

WORKDIR /chemdatawriter

COPY . .

RUN pip install -r requirements.txt

RUN pip install spacy==3.0.7

CMD ["python3.8", "-m", "unittest"]