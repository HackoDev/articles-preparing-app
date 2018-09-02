FROM python:3.6

ENV UUID=1000
ENV WORKDIR=/app

WORKDIR $WORKDIR
ADD requirements.txt .
RUN chmod go+w $WORKDIR && pip install -r requirements.txt gunicorn

USER $UID

ENTRYPOINT ["gunicorn", "wsgi:application", "--bind", "0:8080"]
