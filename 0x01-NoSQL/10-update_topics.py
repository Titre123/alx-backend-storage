#!/usr/bin/env python3
'''Task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    '''return docouments'''
    mongo_collection.update_many({'name': name},
                                {'$set': {'topics': topics}})
