FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /finch
WORKDIR /finch
ADD requirements.txt /finch/
RUN pip install -r requirements.txt
ADD . /finch/
EXPOSE 80
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
