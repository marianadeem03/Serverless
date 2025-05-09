import json
import boto3
from layers.python.utils import (
    update_todo,
    dynamo_db_stream,
)


def lambda_handler(event, context):
    if "Records" in event:
        return dynamo_db_stream(event)

    todo_id = event["pathParameters"]["id"]
    data = json.loads(event.get("body", {}))
    task = data.get("task")
    completed = data.get("completed")

    updated_todo = update_todo(todo_id, task, completed)

    return {"statusCode": 200, "body": json.dumps(updated_todo)}
