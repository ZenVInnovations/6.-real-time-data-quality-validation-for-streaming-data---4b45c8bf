import requests
import json
from kafka import KafkaProducer
import time

API_KEY = 'd4873caa8b5355cefc2c06bc536c42ca'
CITY = 'Bengaluru'
KAFKA_TOPIC = 'weather-data'
KAFKA_SERVER = '127.0.0.1:9092'

# Wait a bit to ensure Kafka broker is ready
time.sleep(10)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

while True:
    weather_data = get_weather()
    print("Sending:", weather_data)
    producer.send(KAFKA_TOPIC, weather_data)
    producer.flush()
    time.sleep(10)
