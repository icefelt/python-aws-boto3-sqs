import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SQS_QUEUE_URL'

# Enable long polling on an existing SQS queue
sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
)