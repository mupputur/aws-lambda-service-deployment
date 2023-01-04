import json


def lambda_handler(event, context):
    customer_id  = event['customers']['id']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "customerID": customer_id,
        }),
    }