FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt

ADD ./src /src
ADD ./scripts /scripts
RUN chmod +x /scripts/wait-for-it.sh
RUN chmod +x /scripts/command-dev.sh
WORKDIR /src
ENTRYPOINT ["/scripts/wait-for-it.sh", "db-svc:3306", "-t", "30", "--", "/scripts/command-dev.sh"]
#CMD ["python3", "manage.py", "migrate"]
#CMD ["python3", "manage.py", "loaddata", "dev"]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
