#!/usr/bin/env python

"""
Simple examples using Redis, MongoDB, and Neo4J
"""

import pymongo
import redis
from neo4j.v1 import GraphDatabase, basic_auth
import configparser

def login_redis_cloud():
    """
        connect to redis and login
    """
    config = configparser.ConfigParser()

    try:
        config.read(".config/config")
        host = config["redis_cloud"]["host"]
        port = config["redis_cloud"]["port"]
        pw = config["redis_cloud"]["pw"]

    except Exception as e:
        print(f'error: {e}')

    try:
        r = redis.StrictRedis(host=host, port=port, password=pw, decode_responses=True)

    except Exception as e:
        print(f'error: {e}')

    return r

def login_mongodb_cloud():
    """
        connect to mongodb and login
    """
    config = configparser.ConfigParser()

    try:
        config.read(".config/config")
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]

    except Exception as e:
        print(f'error: {e}')

    client = pymongo.MongoClient(f'mongodb://{user}:{pw}@cluster0'
        '-shard-00-00-9e7wk.mongodb.net:27017,cluster0-shard-00-01-9e7wk.'
        'mongodb.net:27017,cluster0-shard-00-02-9e7wk.mongodb.net:27017/'
        'test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'
        '&retryWrites=true')

    return client

def login_neo4j_cloud():
    """
        connect to neo4j and login
    """
    config = configparser.ConfigParser()

    try:
        config.read(".config/config")
        user = config["neo4j_cloud"]["user"]
        pw = config["neo4j_cloud"]["pw"]
        connect = config["neo4j_cloud"]["connect"]

    except Exception as e:
        print(f'error: {e}')

    try:
        driver = GraphDatabase.driver(connect, auth=basic_auth(user, pw))

    except Exception as e:
        print(f'error: {e}')

    return driver

def redis_stuff():
    client = login_redis_cloud()
    client.rpush('customer1', 'Bob Dole')
    client.rpush('customer1', '(111) 222-3333')
    client.rpush('customer1', '12345')
    client.rpush('customer2', 'Jane Doe')
    client.rpush('customer2', '(999) 888-7777')
    client.rpush('customer2', '55555')
    client.rpush('customer3', 'Sally Sue')
    client.rpush('customer3', '(555) 444-1234')
    client.rpush('customer3', '98101')
    print(client.lindex('customer2', 2)) # zip code
    print(client.lindex('customer2', 1)) # phone number

def mongo_stuff():
    client = login_mongodb_cloud()
    db = client['dev']
    furniture = db['furniture']
    results = furniture.remove({})

    results = furniture.insert_many([
        {
            'product_type': 'Couch',
            'color': 'Red',
            'in_stock_quantity': 10
        },
        {
            'product_type': 'Couch',
            'color': 'Blue',
            'in_stock_quantity': 3
        },
        {
            'product_type': 'Table',
            'color': 'Mahogany',
            'in_stock_quantity': 5
        }
        ])

    query = {'product_type': 'Couch', 'color': 'Red'}
    results = furniture.find_one(query)

    print(results)

    client.close()

def neo4j_stuff():
    client = login_neo4j_cloud()

    with client.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    with client.session() as session:
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Good'),
                            ('Roland', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Charles', 'Darwin'),
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name:'%s'})" % (first, last)
            session.run(cyph)

        cyph = """MATCH (p: Person)
                RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print ("People in database:")
        for record in result:
            print(record['first_name'], record['last_name'])

        for color in ['red', 'green', 'blue', 'orange', 'yellow', 'indigo', 'violet']:
            cyph = "CREATE (n:Color {name:'%s'})" % (color)
            session.run(cyph)

        cyph = """MATCH (p: Color)
                RETURN p.name as name
                """
        result = session.run(cyph)
        print("Colors in database:")
        for record in result:
            print(record['name'])

        cyph = """MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
                CREATE (p1)-[like:LIKE]->(p2:Color {name: 'red'})
                RETURN p1
                """
        session.run(cyph)

        cyph = """
                MATCH (bob {first_name:'Bob', last_name:'Jones'})
                    -[:LIKE]->(colors)
                RETURN colors
                """
        result = session.run(cyph)
        for record in result:
            print(record)

def main():
    print("REDIS")
    redis_stuff()
    print("")

    print("MONGO")
    mongo_stuff()
    print("")

    print("NEO4J")
    neo4j_stuff()
    print("")

if __name__ == '__main__':
    main()