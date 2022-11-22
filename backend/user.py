import json, boto3
from boto3.dynamodb.conditions import Key
from decimal import *

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def lambda_handler(event, context):
    # TODO implement
    print(event)
    data = json.loads(event['body'])
    #print(event.json)
    #print(event['body'])
    
    # data = {
    #     'id': 'yc393',
    #     'pwd': '1234'
    # }
    user_id = data['id']
    pwd = data['pwd']
    isLry = False
    lryName = ''
    
    temp = table.query(
        KeyConditionExpression = Key('user_id').eq(user_id)
        )
    if temp['Count'] == 1:
        return {
        'statusCode': 200,
        "headers": {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps('Already exist', cls=DecimalEncoder)
    }
    #print(temp)
    
    res = table.put_item(
            Item = {
                'user_id': user_id,
                'pwd': pwd,
                'isLry': isLry, 
                'lryName': lryName
            })
    return {
        'statusCode': 200,
        "headers": {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps('success')
    }
