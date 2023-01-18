#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        print('\tmethod {}: {}'.format(method, logs.
              nginx.count_documents({'method': method})))
    print('{} status check'.format(logs.nginx.count_documents(
        {'method': 'GET', 'path': '/status'})))
