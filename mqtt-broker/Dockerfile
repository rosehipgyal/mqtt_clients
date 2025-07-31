FROM python:3.11-slim

WORKDIR /app

COPY mqtt_client.py .

RUN pip install --no-cache-dir paho-mqtt

CMD ["python", "mqtt_client.py"]
