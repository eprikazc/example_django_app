FROM python:3.7.5

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./proj /proj
WORKDIR /proj
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "proj.wsgi" ]
