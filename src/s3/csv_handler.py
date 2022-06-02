import csv
import io

def res2CsvDict(response):
    data = response['Body'].read()
    try:
        file_contents = io.TextIOWrapper(io.BytesIO(data))
        reader = csv.DictReader(file_contents)
        csv_dict = [row for row in reader]
        return csv_dict
    except Exception as e:
        print(e)
        print('error on read as csv')
        raise e
