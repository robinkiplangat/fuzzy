FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /fuzzy

WORKDIR /fuzzy

ADD requirements.txt /fuzzy/

RUN pip install -r requirements.txt

EXPOSE 80

EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
