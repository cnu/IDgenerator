FROM python:3.6
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /wccg
WORKDIR /wccg
EXPOSE 8000
CMD ["python", "wccg/manage.py", "runserver", "0.0.0.0:8000"]