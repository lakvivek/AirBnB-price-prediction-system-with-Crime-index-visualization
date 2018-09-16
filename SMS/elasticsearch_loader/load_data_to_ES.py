import urllib, json
import subprocess
import re
import csv
from elasticsearch import Elasticsearch, RequestsHttpConnection

file = "../data/processed_NYPD"


with open('../data/{}.json'.format(file)) as f:
    data = json.load(f)


esEndPoint = "search-sms-3qmuiazwjvut4ms6j4nke3cjcm.us-east-1.es.amazonaws.com"

try:
    esClient = Elasticsearch(
        hosts=[{'host': esEndPoint, 'port': 443}],
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
        )
    for record in data:
        esClient.index(index="crime", doc_type="hit", body=json.dumps(record))
except Exception as exception:
    print(exception)
