import os
import configparser
from posting_content import videoPublishing


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

    return col

def readConfigFile():
    parser = configparser.ConfigParser()
    parser.read("Config.ini")
    return parser


if __name__ == '__main__':
    # Load the Parser with configuration variables from the config file
    parser = readConfigFile()

    connectionString = parser.get("configDB", "CONNECTION_STRING")
    connectionName = parser.get("configDB", "COLLECTION_NAME")
    databaseName = parser.get("configDB", "DATABASE_NAME")

    # Get the database
    db = get_database(connectionString, connectionName, databaseName)
    db_select = db.find_one({'uploaded': False})
    video_url = db_select['video_url']
    video_caption = db_select['caption']
    print('Uploading Video :' + video_url)
    print('Video Caption :' + video_caption)

    uploadedStatus = videoPublishing(video_url, video_caption)

    db.update_one(db_select, {"$set": {'uploaded': True}})


