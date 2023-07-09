import boto3

def lambda_handler(event, context):
    # Conexión al servicio de DynamoDB
    dynamodb = boto3.resource('dynamodb')

    # Selección de la tabla 'UserTable'
    table = dynamodb.Table('UserTable')

    # Escaneo de la tabla para obtener todos los elementos
    response = table.scan()

    # Extracción de los elementos escaneados
    items = response['Items']

    # Devolución de la respuesta con código de estado HTTP 200 y elementos escaneados
    return {
        'statusCode': 200,
        'pendientes': items
    }
