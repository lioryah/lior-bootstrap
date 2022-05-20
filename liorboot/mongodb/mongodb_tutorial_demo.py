# from pymongo import MongoClient
import pymongo
import dns
import datetime
import fire
from pathlib import Path



def pymongo_demo(connection_conf:str):
    if connection_conf == "cluster0":
        # Replace the uri string with your MongoDB deployment's connection string.
        conn_str = 'mongodb+srv://lior:lior123@cluster0.xeqbp.mongodb.net/test?retryWrites=true&w=majority'

        # set a 5-second connection timeout
        client = pymongo.MongoClient(conn_str)
        db = client.test
    
    if connection_conf == "datalake0":
        client = pymongo.MongoClient("mongodb://lior:lior123@datalake0-xeqbp.a.query.mongodb.net/myFirstDatabase?ssl=true&authSource=admin")
        db = client.test

    try:
        print("server information")
        print(client.server_info())
    except Exception:
        print("Unable to connect to the server.")

    # add_person_doc(client)
    upload_data_from_file("2466_tokens.txt" , client)

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

    print("Done with uploading from file {}", file_name)

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


def _main():
    pymongo_demo("cluster0")

if __name__ == '__main__':
    _main()