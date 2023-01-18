#!/usr/bin/env python3
'''Task 8's module.
'''


def list_all(mongo_collection):
    '''
        return documents
    '''
    if (mongo_collection == {}):
        return []
    return mongo_collection.find({})
