from kafka import KafkaConsumer

consumer = KafkaConsumer('kafkaTest')
for msg in consumer:
    print(msg)
    122131