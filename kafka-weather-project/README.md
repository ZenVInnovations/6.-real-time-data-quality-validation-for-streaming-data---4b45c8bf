# Kafka Weather Project

A simple Kafka-based weather data streaming application using OpenWeather API.

## Components

- **Producer**: Fetches weather data and sends to Kafka topic.
- **Consumer**: Listens to the Kafka topic and prints weather data.
- **Kafka Configs**: Kafka and producer configuration files.

## Setup

1. Install dependencies:
   ```bash
   pip install kafka-python requests
   ```

2. Start Zookeeper and Kafka server.

3. Run the producer:
   ```bash
   python src/producer.py
   ```

4. Run the consumer:
   ```bash
   python src/consumer.py
   ```

## Notes

- Kafka must be running locally on `localhost:9092`.
- Adjust `CITY` and `API_KEY` in `producer.py` as needed.
