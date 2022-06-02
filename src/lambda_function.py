import s3.client
import s3.csv

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    response = s3.client.fetch_binary(event)
    csv_dict = s3.csv.res2CsvDict(response)
    print(csv_dict)

    return response['ContentType']

