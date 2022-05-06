import boto3
import botocore.exceptions
import json
from cgi import parse_header, parse_multipart
from io import BytesIO


def lambda_handler(event, context):

    c_type, c_data = parse_header(event['headers']['Content-Type'])
    assert c_type == 'multipart/form-data'
    form_data = parse_multipart(BytesIO(event['body'].decode('base64')), c_data)

    print(form_data)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }