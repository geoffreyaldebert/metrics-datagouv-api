FROM python:3.9


COPY ./ /srv/flask
WORKDIR /srv/flask

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "app.py" ] 