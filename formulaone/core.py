# -*- coding: utf-8 -*-

import boto3
session = boto3.Session(
    aws_access_key_id = 'AKIAU4GCMVBSY62NF4CQ',
    aws_secret_access_key = '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'
)

dynamo_resource = session.resource(
    'dynamodb',
    region_name='eu-west-1'
)

tables = []
for table in dynamo_resource.tables.all():
    print(table.name)
    tables.append(table)

movies = dynamo_resource.Table('doc-example-table-movies')
movies.get_item(Key={'year': 2013, 'title': '2 Guns'})

from boto3.dynamodb.conditions import Key
movies.query(
    KeyConditionExpression=Key('year').eq(2013)
)