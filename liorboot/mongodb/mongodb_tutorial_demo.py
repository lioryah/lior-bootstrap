# from pymongo import MongoClient
from matplotlib.collections import Collection
import pymongo
import dns
import datetime
import fire
from pathlib import Path


# return pymongo client_db 
def pymongo_demo(connection_conf:str, db_name:str):
    if connection_conf=="cluster0" and db_name=="tokens":
        # Replace the uri string with your MongoDB deployment's connection string.
        conn_str = 'mongodb+srv://lior:lior123@cluster0.xeqbp.mongodb.net/tokens?retryWrites=true&w=majority'

        # set a 5-second connection timeout
        client = pymongo.MongoClient(conn_str)
    
    if connection_conf == "datalake0":
        client = pymongo.MongoClient("mongodb://lior:lior123@datalake0-xeqbp.a.query.mongodb.net/myFirstDatabase?ssl=true&authSource=admin")

    try:
        print("server information: \n\n")
        print(client.server_info())
    except Exception:
        print("Unable to connect to the server.")

    return client


def add_person_doc(client:pymongo.MongoClient):
    db = client.gettingStarted

    people = db.people

    personDocument = {
        "name": {"first": "Ice", "last": "Cube"},
        "views": 1250000
    }

    people.insert_one(personDocument)

    print(people.find_one({"name.last": "Yahav"}))


def upload_data_from_file(file_name:str, client:pymongo.MongoClient):
    db = client.tokens

    tokens = db.tokens2466
    
    data_file = open(file_name, "r")
    data = data_file.readlines()
    
    for data_entry in data:
        print(data_entry)
        tokens.insert_one({"token":data_entry.strip()})

    data_file.close()
    print(f"Done with uploading from file {file_name}")


def upload_data_from_file_generator(file_name:str, client:pymongo.MongoClient):
    db = client.tokens

    tokens = db.tokens2466
    
    tokens.insert_one(next(get_data_from_file_generator(file_name)))
    

def get_data_from_file_generator(file_name:str):
    data_file = open(file_name, "r")
    data = data_file.readlines()
    data_entry = data

    while data_entry!=None:
        yield data_entry


def delete_many(client:pymongo.MongoClient, collection_name:str):
    # db = client.tokens
    # db = client.tokens

    # tokens = db.tokens2466
   
    # db.{collection}.delete_many({})
    if collection_name=="2466tokens":
        client.tokens2466.delete_many({})

def _main():
    client = pymongo_demo("cluster0", "tokens")
   
    # add_person_doc(client)
    
    # file_name = "2466_tokens.txt"
    # upload_data_from_file(file_name , client)
    
    file_name = "10_tokens.txt"
    upload_data_from_file(file_name , client)

    delete_many(client, "tokens2466")


if __name__ == '__main__':
    _main()