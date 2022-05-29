# from matplotlib.collections import Collection
# from matplotlib import collections
# import dns
# import datetime
# import fire
# import typing

import pymongo
from pathlib import Path
import json


# return pymongo client_db 
def pymongo_demo(connection_conf:str):
    if connection_conf=="cluster0":
        # Replace the uri string with your MongoDB deployment's connection string.
        conn_str = 'mongodb+srv://lior:lior123@cluster0.xeqbp.mongodb.net/?retryWrites=true&w=majority'
        client = pymongo.MongoClient(conn_str)
    
    if connection_conf == "datalake0":
        client = pymongo.MongoClient("mongodb://lior:lior123@datalake0-xeqbp.a.query.mongodb.net/?ssl=true&authSource=admin")

    try:
        print("\n --- server information: --- \n")
        print(client.server_info())
    except Exception:
        print("Unable to connect to the server.")

    return client


def upload_data_from_file(file_name:str, client:pymongo.MongoClient, db_name:str, coll_name:str):
    curr_coll = client[db_name][coll_name]
    data_file = open(file_name, "r")
    data = data_file.readlines()
    
    for data_entry in data:
        print(data_entry)
        curr_coll.insert_one({"token":data_entry.strip()})

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

def get_db_coll_user() -> list[str]:
    db_name = input("databse name:\n")
    coll_name = input("collection name:\n")
    return [db_name, coll_name]
    
    
def _main():
    # creating a mongodb client which connects with datalake0
    # client = pymongo_demo("datalake0")
    # add_person_doc(client)
    
    # "-------------------------------"

    # creating a mongodb client which connects with cluster0
    client = pymongo_demo("cluster0")

    menu_msg = '''          
    1. add a new db
    2. add a new collection
    3. add document(document) - create
    4. get ducument({filter,value}) - read
    5. update document({field,value}) - update
    6. delete document by id(uid)
    7. get database list
    8. delete all documents
    9. add documents from file(file.txt)
    '''
    # [db_name, coll_name] = get_db_coll_user()
    [db_name, coll_name] = ["tokens", "tokens2466"]
    curr_coll = client[db_name][coll_name]
    
    choice = int(input(menu_msg))
    if choice==1:
        pass
   
    elif choice==2:
        pass
    
    elif choice==3: # add document(document) - create
        try:
            document = json.loads(input("enter document (in json format): \n"))
            curr_coll.insert_one(document)
        except:
            print("Wrong input. make sure to enter document in json format")
    
    elif choice==4: # get ducument({filter,value}) - read
        try:
            filter = input("filter:\n")
            value = input("value:\n")
            print(curr_coll.find_one({filter: value}))
        except:
            print("Wrong input. make sure you enter proper filter and value")
    
    elif choice==5: # update document({field,value}) - update
        curr_coll.update_many
    
    elif choice==6:
        pass
    
    elif choice==7: # get database list
        print(client.list_database_names())
   
    elif choice==8: # delete all documents
        curr_coll.delete_many({})
 
    elif choice==9:
        try:
            file_name = input("file name:\n")
            # file_name = "10_tokens.txt"
            upload_data_from_file(file_name , client, db_name, coll_name)
        except (FileNotFoundError):
            print("File was not found")
  
    else:
        print("invalid option")


if __name__ == '__main__':
    _main()