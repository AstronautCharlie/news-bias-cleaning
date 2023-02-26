import boto3 

dynamodb = boto3.resource('dynamodb')
stories = dynamodb.Table('stories')
items = stories.scan()