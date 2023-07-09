import boto3

def lambda_handler(event, context):
    # Entrada
    username = event['username']
    phone_number = event['phone_number']
    password = event['password']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UserTable')

    # Verificar si el número de teléfono ya existe
    response = table.scan(
        FilterExpression='phone_number = :phone_number',
        ExpressionAttributeValues={':phone_number': phone_number},
        ProjectionExpression='id'
    )

    if response['Items']:
        return {
            'statusCode': 400,
            'message': 'El número de teléfono ya está en uso'
        }

    # Verificar si el nombre de usuario ya existe
    response = table.scan(
        FilterExpression='username = :username',
        ExpressionAttributeValues={':username': username},
        ProjectionExpression='id'
    )

    if response['Items']:
        return {
            'statusCode': 400,
            'message': 'El nombre de usuario ya está en uso'
        }

    # Obtener el último valor de la ID
    response = table.scan(
        ProjectionExpression='id',
        Limit=1,
        ConsistentRead=True
    )

    last_id = 0
    if response['Items']:
        last_id = response['Items'][0]['id']

    # Incrementar la ID
    new_id = last_id + 1

    # Insertar el nuevo elemento en la tabla
    data = {
        'id': new_id,
        'username': username,
        'phone_number': phone_number,
        'password': password
    }
    table.put_item(Item=data)

    # Salida
    return {
        'statusCode': 200,
        'pendienteInsertado': data
    }
