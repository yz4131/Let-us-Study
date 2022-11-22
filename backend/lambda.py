import json, boto3
from boto3.dynamodb.conditions import Key
from decimal import *

#client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CountingBoard')
user_table = dynamodb.Table('user')


lib_name = {'bl', 'aanfal', 'bcl', 'bnel', 'eal', 'hsl', 'jl', 'll', 'sipa', 'ml', 'mal', 'sel', 'tc'}

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def init(bl, aanfal, bcl, bnel, eal, hsl, jl, ll, sipa, ml, mal, sel, tc):
    lib = [bl, aanfal, bcl, bnel, eal, hsl, jl, ll, sipa, ml, mal, sel, tc]
    lib_name = ['bl', 'aanfal', 'bcl', 'bnel', 'eal', 'hsl', 'jl', 'll', 'sipa', 'ml', 'mal', 'sel', 'tc']
    for i in range(13):
        res = table.put_item(
            Item = {
                'name': lib_name[i],
                'capacity': lib[i],
                'empty': lib[i], 
                'occupied': 0
            })

    return res 
    
def clear():
    scan = table.scan(
    ProjectionExpression='#k',
    ExpressionAttributeNames={
        '#k': 'name'
    }
)
    
    
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(Key=each)

# table.update_item(
#     Key={'pkey': 'asdf12345'},
#     AttributeUpdates={
#         'status': 'complete',
#     },
# )
def enter(name, user_id, pwd):
    if name not in lib_name:
        return "Not a valid name"
    data = user_table.query(
        KeyConditionExpression = Key('user_id').eq(user_id)
        )['Items'][0]
    print(data)
    if pwd != data['pwd']:
        return "wrong password"
    if data['isLry']:
        return "already entered, please log off first"
    cur = get_by_name(name)[0]
    print(cur)
    occupied = cur['occupied']
    empty = cur['empty']
    user_table.update_item(
            Key = {"user_id": user_id},
            UpdateExpression = "set #isLry=:b, #lryName=:n",
            ExpressionAttributeNames = {
                '#isLry': 'isLry',
                '#lryName': 'lryName'
            },
            ExpressionAttributeValues = {
                ':b': True,
                ':n': name
            },
            ReturnValues="UPDATED_NEW"
            )
    #print()
    if empty > 0:
        res = table.update_item(
            Key = {'name': name},
            UpdateExpression="set #empty=:e, #occupied=:o",
            ExpressionAttributeNames={
                '#empty': 'empty',
                '#occupied': 'occupied',
            },
            ExpressionAttributeValues={
        ':e': Decimal(str(empty - 1)),
        ':o': Decimal(str(occupied + 1)),
            },
            ReturnValues="UPDATED_NEW"
    )
        #print(res)
        return 'success'
    else:
        res = table.update_item(
            Key = {'name': name},
            UpdateExpression="set #occupied=:o",
            ExpressionAttributeNames={
                '#occupied': 'occupied',
            },
            ExpressionAttributeValues={
        ':o': Decimal(str(occupied + 1)),
            },
            ReturnValues="UPDATED_NEW"
            )
        return 'success'
    
def leave(id, pwd):
    data = user_table.query(
        KeyConditionExpression = Key('user_id').eq(id)
        )['Items'][0]
    if pwd != data['pwd']:
        return "wrong password"
    if not data['isLry']:
        return "User hasn't enter any library"
    name = data['lryName']
    if name not in lib_name:
        return "Not a valid name"
    user_table.update_item(
            Key = {"user_id": id},
            UpdateExpression = "set #isLry=:b, #lryName=:n",
            ExpressionAttributeNames = {
                '#isLry': 'isLry',
                '#lryName': 'lryName'
            },
            ExpressionAttributeValues = {
                ':b': False,
                ':n': ''
            },
            ReturnValues="UPDATED_NEW"
            )
    cur = get_by_name(name)[0]
    #print(cur)
    occupied = cur['occupied']
    empty = cur['empty']
    capacity = cur['capacity']
    #print()
    if occupied == 0:
        return 'invalid exit'
    if occupied <= capacity:
        res = table.update_item(
            Key = {'name': name},
            UpdateExpression="set #empty=:e, #occupied=:o",
            ExpressionAttributeNames={
                '#empty': 'empty',
                '#occupied': 'occupied',
            },
            ExpressionAttributeValues={
        ':e': Decimal(str(empty + 1)),
        ':o': Decimal(str(occupied - 1)),
            },
            ReturnValues="UPDATED_NEW"
    )
        #print(res)
        return 'success'
    else:
        res = table.update_item(
            Key = {'name': name},
            UpdateExpression="set #occupied=:o",
            ExpressionAttributeNames={
                '#occupied': 'occupied',
            },
            ExpressionAttributeValues={
        ':o': Decimal(str(occupied - 1)),
            },
            ReturnValues="UPDATED_NEW"
            )
        return 'success'
    
    
    

def get_all():
    lib_name = ['bl', 'aanfal', 'bcl', 'bnel', 'eal', 'hsl', 'jl', 'll', 'sipa', 'ml', 'mal', 'sel', 'tc']
    res = {}
    for i in range(13):
        #temp = 
        res[lib_name[i]] = get_by_name(lib_name[i])[0]
    return res
        

def get_by_name(name):
    res = table.query(
        KeyConditionExpression = Key('name').eq(name)
        )
    #print(res['Items'][0]['capacity'])
    return res['Items']
    
def get_by_sort(val):
    res = table.scan(
        FilterExpression = Key('empty').gt(val)
        )
    #print(res)
    #print(res)
    return res['Items']
         

def lambda_handler(event, context):
    # TODO implement
    print(event)
    res = {}
    #leave('yc3993')
    #clear()
    #init(1000, 100, 300, 200, 200, 200, 200, 200, 200, 200, 200, 500, 300)
    #enter('bcl', 'yc3993')
    
    try:
        if event['path'] == '/count':
            if not event["queryStringParameters"]:
                res = get_all()
            elif 'name' in event["queryStringParameters"]: 
                name = event["queryStringParameters"]['name']
                res = get_by_name(name)
            elif 'value' in event["queryStringParameters"]:
                value = int(event["queryStringParameters"]['value'])
            #print(value)
                res = get_by_sort(value)
        elif event['path'] == '/enter':
            name = event["queryStringParameters"]['name']
            id = event["queryStringParameters"]["id"]
            pwd = event["queryStringParameters"]['pwd']
            print(name, id, pwd)
            res = enter(name, id, pwd)
        elif event['path'] == '/leave':
            #print(1)
            id = event["queryStringParameters"]['id']
            pwd = event["queryStringParameters"]['pwd']
            print(id, pwd)
            res = leave(id, pwd)
            print(res)
            #return res
        
    except:
        res = 'Cannot get information'
        
    #print(init(1000, 100, 300, 200, 200, 200, 200, 200, 200, 200, 200, 500, 300))
    #print(get_by_name('bcl'))
    #get_by_sort(300)
    #get_all()
    
    
    return {
        'statusCode': 200,
        "headers": {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(res, cls=DecimalEncoder)
    }
