FROM alpine:latest
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8080
# CMD [ "echo", "Hello world" ]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]