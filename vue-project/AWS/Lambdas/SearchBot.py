import boto3

def lambda_handler(event, context):
    # Entrada
    bot_username = event['bot_username']
    icon = event['icon']
    owner = event['owner']
    description = event['description']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BotTable')

    # Verificar si el bot_username ya existe en la tabla
    response = table.scan(
        FilterExpression='bot_username = :username',
        ExpressionAttributeValues={':username': bot_username}
    )

    if response['Items']:
        return {
            'statusCode': 400,
            'body': 'El bot_username ya existe. Proporciona un valor único.'
        }

    # Obtener el último valor de la ID
    response = table.scan(
        ProjectionExpression='bot_id',
        Limit=1,
        ConsistentRead=True
    )

    last_bot_id = 0
    if response['Items']:
        last_bot_id = response['Items'][0]['bot_id']

    # Incrementar la ID
    new_bot_id = last_bot_id + 1
    
    # Insertar el nuevo elemento en la tabla
    data = {
        'bot_id': new_bot_id,
        'bot_username': bot_username, 
        'icon': icon,
        'owner': owner,
        'description': description        
    }
    table.put_item(Item=data)

    # Salida
    return {
        'statusCode': 200,
        'bot': data
    }
