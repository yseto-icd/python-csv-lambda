import s3.client
import s3.csv_handler
import db.client

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    response = s3.client.fetch_binary(event)
    csv_dict = s3.csv_handler.res2CsvDict(response)
    print(csv_dict)
    conn = db.client.connect()
    db.client.insert(conn, csv_dict)

    return response['ContentType']
