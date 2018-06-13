#!/usr/bin/env python

"""
Login to Redis, MongoDB, or Neo4J database using config file
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