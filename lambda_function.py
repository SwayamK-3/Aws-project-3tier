import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("FeedbackTable")   # change table name if needed

def lambda_handler(event, context):

    # Get JSON body from API Gateway
    try:
        body = json.loads(event.get("body", "{}"))
    except:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "invalid json"})
        }

    name = body.get("name")
    email = body.get("email")
    feedback = body.get("feedback")

    # CHECK if all fields exist
    if not name or not email or not feedback:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "missing fields"})
        }

    # Insert into DynamoDB
    table.put_item(
        Item={
            "id": str(int(time.time() * 1000)),
            "name": name,
            "email": email,
            "feedback": feedback
        }
    )

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"message": "Feedback submitted successfully!"})
    }
