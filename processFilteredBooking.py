import json
import os
import boto3
import csv
from io import StringIO
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ['OUTPUT_BUCKET_NAME']
    key = 'filtered_booking_data.csv'  

    
    new_record = json.loads(event[0]['body'])
    print(new_record)

    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        csv_content = response['Body'].read().decode('utf-8')
        csv_buffer = StringIO(csv_content)
        reader = list(csv.DictReader(csv_buffer))
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            # file doesn't exist yet
            reader = []
        else:
            raise

    
    reader.append(new_record)

    # write all records back to CSV
    fieldnames = ["bookingId", "userId", "propertyId", "location", "startDate", "endDate", "price", "duration"]
    output_buffer = StringIO()
    writer = csv.DictWriter(output_buffer, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reader)

    # upload updated CSV to S3
    s3.put_object(Bucket=bucket_name, Key=key, Body=output_buffer.getvalue())

    return {
        'statusCode': 200,
        'body': json.dumps('CSV updated in S3')
    }
