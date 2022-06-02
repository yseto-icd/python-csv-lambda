import urllib.parse
import csv
import boto3
import io

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
    try:
        data = response['Body'].read()
        contents = data.decode('utf-8')
        print("contents: " + contents)
    except Exception as e:
        print(e)
        print('error on printing')
        raise e
    try:
        file_contents = io.TextIOWrapper(io.BytesIO(data))
        reader = csv.DictReader(file_contents)
        l = [row for row in reader]
        print(l)
    except Exception as e:
        print(e)
        print('error on read as csv')
        raise e
    return response['ContentType']
