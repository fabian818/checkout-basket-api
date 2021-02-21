FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD source/requirements.txt /code/
ADD .pylintrc /code/
ADD test.sh /code/
RUN pip install -r requirements.txt
ADD source/. /code
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
