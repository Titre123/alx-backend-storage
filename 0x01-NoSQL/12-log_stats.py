#!/usr/bin/env python3
'''Task 12'''


import pymongo


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = my_client['logs']
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('{} logs'.format(logs.nginx.count_documents({})))
    print('Methods:')
    for method in methods:
        print('\tmethod {}: {}'.format(method, logs.
              nginx.count_documents({'method': method})))
    print('{} status check'.format(logs.nginx.count_documents(
        {'method': 'GET', 'path': '/status'})))
