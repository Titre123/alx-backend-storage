#!/usr/bin/env python3
'''Task 9's module.
'''


def insert_school(mongo_collection, **kwargs):
    '''return docouments'''
    return mongo_collection.insert_one(kwargs).inserted_id
