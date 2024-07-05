import pandas as pd
import json

def lambda_handler(event, context):
    print('Done x1.1')
    if event and isinstance(event, dict):
        input_data = event
    elif event and isinstance(event, str):
        input_data = json.loads(event)
    else:
        input_data = {"a": "default", "b": "default", "c": "default"}

    return input_data.get("a", 'a not found')