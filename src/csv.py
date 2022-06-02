import csv
import s3_client
import io

print('Loading function')



def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    response = s3_client.fetch_binary(event)

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
