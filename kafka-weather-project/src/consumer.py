from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'weather-data',
    bootstrap_servers=['127.0.0.1:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Waiting for messages...")

for message in consumer:
    print("Received:", message.value)
