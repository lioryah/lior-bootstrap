
import pymongo
import dns
import datetime


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

    
    db = client.gettingStarted

    people = db.people

    personDocument = {
        "name": {"first": "Alan", "last": "Turing"},
        "birth": datetime.datetime(1912, 6, 23),
        "death": datetime.datetime(1954, 6, 7),
        "contribs": ["Turing machine", "Turing test", "Turingery"],
        "views": 1250000
    }

    personDocument2 = {
        "name": {"first": "Lior", "last": "Yahav"},
        "birth": datetime.datetime(1987, 10, 13),
        "views": 123456
    }

    # people.insert_one(personDocument2)

    print(people.find_one({"name.last": "Yahav"}))



def _main():
    pymongo_demo("cluster0")

if __name__ == '__main__':
    _main()