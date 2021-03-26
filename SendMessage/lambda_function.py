import json
import nexmo
import python-dotenv

client = nexmo.Client(key=key, secret=secret)

client.send_message({
    'from': '18335271670',
    'to': '19735243077',
    'text': 'Hello from Vonage SMS API',
})

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
