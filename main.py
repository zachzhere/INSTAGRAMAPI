import time as t
import time

from instabot import Bot

from pymongo import MongoClient
import pymongo

import os
import dns
from pathlib import Path
import configparser
import ffmpeg
from posting_content import videoPublishing
from instapy_cli import client
from pymongo import MongoClient

import sys
from pprint import pprint  # for printing Python dictionaries in a human-readable way

if os.path.isfile("path/to/config/file.json"):
    os.remove("path/to/config/file.json")


def get_database(connectionString, collectionName, DatabaseName):
    from pymongo import MongoClient
    import pymongo

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(connectionString)
    db = client[collectionName]
    col = db[DatabaseName]
    x = col.find()
    for data in x:
        print(data)
    # Create the database for our example (we will use the same database throughout the tutorial
    return col


def readConfigFile():
    parser = configparser.ConfigParser()
    parser.read("Config.ini")
    return parser


if __name__ == '__main__':
    # Load the Parser with configuration variables from the config file
    parser = readConfigFile()

    connectionString = parser.get("config", "CONNECTION_STRING")
    connectionName = parser.get("config", "COLLECTION_NAME")
    databaseName = parser.get("config", "DATABASE_NAME")

    # Get the database
    db = get_database(connectionString, connectionName, databaseName)
    db_select = db.find_one({'uploaded': False})
    video_url = db_select['video_url']
    video_caption = db_select['caption']
    print(video_url)
    print(video_caption)

    uploadedStatus = videoPublishing(video_url, video_caption)

    db.update_one(db_select, {"$set": {'uploaded': True}})

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
