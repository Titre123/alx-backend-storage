#!/usr/bin/env python3
'''Task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    '''return docouments'''
    mongo_collection.insert_one({'name': 'Holberton'},
                                {'$set': {'topics': topics}})
