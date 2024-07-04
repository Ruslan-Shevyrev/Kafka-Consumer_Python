from kafka import KafkaConsumer

bootstrap_servers = ''
group_id = 'test1'
topics = ["test"]
key = b'111'
value = b'{"test": 123}'

consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
						group_id=group_id,
						auto_offset_reset="earliest",
						enable_auto_commit=False)

consumer.subscribe(topics)

for message in consumer:
	try:
		consumer.commit()
	except Exception as e:
		print('Kafka commit error, continue')
		time.sleep(1)
		continue
	
	try:
		print(message.value.decode('utf-8'))
	except Exception as e:
		print(f"Error occurred while consuming messages: {e}")
	finally:
		consumer.close()
