import boto3
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='my_queue'
 
 )
print("Created queue '%s' with URL=%s",'my_queue',queue.url)

import config

def send_message(queue_url):
    sqs_client = boto3.client("sqs")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl=f"https://sqs.us-east-2.amazonaws.com/837507203799/my_queue,/{config.QUEUE_NAME}",
        MessageBody=json.dumps(message)
    )
    print(response)

    send_message("Hello, world!")