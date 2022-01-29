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

    dbLists = client[collectionName]  # Gets the list of Databases in the collection

    col = dbLists[DatabaseName]  # Gets the info contained in the database

    x = col.find()

    return col


def readConfigFile():
    parser = configparser.ConfigParser()
    parser.read("Config.ini")
    return parser


if __name__ == '__main__':
    parser = readConfigFile()  # Load the Parser with configuration variables from the config file

    #  Initialize config variable from the config file
    connectionString = parser.get("configDB", "CONNECTION_STRING")
    connectionName = parser.get("configDB", "COLLECTION_NAME")
    databaseName = parser.get("configDB", "DATABASE_NAME")

    db = get_database(connectionString, connectionName, databaseName)  # Get the database

    db_select = db.find_one({'uploaded': False})  # Gets first item stored in database that has not been uploaded

    video_url = db_select['video_url']  # Gets the video url associated with the index

    video_caption = db_select['caption']  # Gets the caption associated with the index

    print('Uploading Video :' + video_url)
    print('Video Caption :' + video_caption)

    uploadedStatus = videoPublishing(video_url, video_caption)  # Upload video from db

    db.update_one(db_select, {"$set": {'uploaded': True}})
