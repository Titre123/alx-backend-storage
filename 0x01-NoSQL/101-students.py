#!/usr/bin/env python3
'''Task 14's module.
'''


def top_students(mongo_collection):
    return mongo_collection.aggregate([
        {
            '$project':
            {
                '_id': 1, 'name': 1,
                'averageScore': {
                    '$avg': {
                        '$avg': 'topics.score'
                        }
                    },
                'topics': 0
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ])
