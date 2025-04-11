# lambda code to generate ramdom data like mock_data.json and send it to SQS

import json
import os
import random
import time
from datetime import datetime
import boto3


def lambda_handler(event, context):
    # Initialize SQS client
    sqs = boto3.client('sqs')
    
    # Get the queue URL from environment variable
    queue_url = os.environ['QUEUE_URL']

    for i in range(10):
        start_timestamp = time.time()
        end_timestamp = start_timestamp + random.randint(1, 30) * 86400  # Add 1 to 30 days

        start_date_str = time.strftime("%Y-%m-%d", time.localtime(start_timestamp))
        end_date_str = time.strftime("%Y-%m-%d", time.localtime(end_timestamp))

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        duration = (end_date - start_date).days

        data = {
            "bookingId": str(random.randint(100000, 999999)),
            "userId": str(random.randint(1000, 9999)),
            "propertyId": str(random.randint(10000, 99999)),
            "location": f"{random.choice(['Delhi', 'Kolkata', 'Bangaluru'])}, {random.choice(['USA', 'Canada', 'Mexico'])}",
            "startDate": start_date_str,
            "endDate": end_date_str,
            "price": str(random.randint(100, 500)),
            "duration": duration
        }
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(data)
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SQS!')
    }