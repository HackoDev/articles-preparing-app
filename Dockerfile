FROM python:3.6

ARG UUID=1000
ENV WORKDIR=/app

WORKDIR $WORKDIR
ADD requirements.txt .
RUN chmod go+w $WORKDIR && pip install -r requirements.txt gunicorn

USER $UUID

ENTRYPOINT ["gunicorn", "wsgi:application", "--bind", "0:8080"]
