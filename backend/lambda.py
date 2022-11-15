import json, boto3
from boto3.dynamodb.conditions import Key
#client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CountingBoard')

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

def get_by_name(name):
    res = table.query(
        KeyConditionExpression = Key('name').eq(name)
        )
    print(res)
    return res['Items']
    
def get_by_sort(val):
    res = table.query(
        IndexName = 'empty-index',
        KeyConditionExpression = Key('empty').lt(val)
        )
    #print(res)
    print(res)
         

def lambda_handler(event, context):
    # TODO implement
    print(event)
    #print(init(1000, 100, 300, 200, 200, 200, 200, 200, 200, 200, 200, 500, 300))
    #print(get_by_name('bcl'))
    get_by_sort(300)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
