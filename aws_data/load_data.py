# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

def get_data():
    load_dotenv()

    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

    import boto3
    session = boto3.Session(
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    dynamo_resource = session.resource(
        'dynamodb',
        region_name='eu-west-1'
    )
    # dynamo_resource = get_dynamo_resource()

    tables = []
    for table in dynamo_resource.tables.all():
        print(table.name)
        tables.append(table)

    movies = dynamo_resource.Table('doc-example-table-movies')
    movies.get_item(Key={'year': 2013, 'title': '2 Guns'})

    from boto3.dynamodb.conditions import Key
    movie_data = movies.query(
        KeyConditionExpression=Key('year').eq(2013)
    )

    # print(movie_data)

    # write to file as txt
    # with open('movie_data.txt', 'w') as f:
    #     f.write(str(movie_data))

get_data()