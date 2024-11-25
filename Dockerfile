FROM python:3.14.0a2-slim

RUN apt-get update && apt-get upgrade
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY app /app

RUN useradd app
USER app

WORKDIR "/app"
ENTRYPOINT ["python", "/app/main.py"]
CMD ["-h"]