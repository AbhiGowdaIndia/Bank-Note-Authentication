FROM python:3.7

ARG target="H:/AI Projects/Docker_Imgs/"

COPY . ${target}

EXPOSE 5000

WORKDIR ${target}

RUN pip install -r requirements.txt

CMD python flask_api_flasgger.py