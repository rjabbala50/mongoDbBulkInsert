'''
... Description: This scripts bulk uploads documents to collections in mongodb
... @author Vrushali V
... @since September 15, 2021, 2.30 AM IST 
'''
import json

COLLECTION_NAME   = "MyFirstDatabase"
CLUSTER_NAME      = "cluster0.gxrbo.mongodb.net"
MONGO_PREFIX      = "mongodb+srv"
DATABASE_NAME     = "My_shopping_list"
DATABASE_USERNAME = "m001-student"
DATABASE_PASSWORD = "m001-mongodb-basics"
COLLECTION_MAX_SIZE = 2 #Working only for 2, debug later for bulk inserts.  
SCHEMA_FILE       = '/home/ec2-user/PythonTutorial/bulkimport.schema' 

def get_database(): 
    from pymongo import MongoClient
    import pymongo 

    CONNECTION_URL=MONGO_PREFIX+"://"+DATABASE_USERNAME+":"+DATABASE_PASSWORD+"@"+CLUSTER_NAME+"/"+DATABASE_NAME

    from pymongo import MongoClient 
    client = MongoClient(CONNECTION_URL)
    return client[DATABASE_NAME]

if __name__ == "__main__" :
    dbname = get_database()
    collection_name = dbname[COLLECTION_NAME]
    #read schema from file 
    documents = []
    f = open(SCHEMA_FILE,"r")
    data = json.loads(f.read())
    for document in data['MyFirstDatabase'] :
        documents.append(document)
    f.close()
    count = 1
    while count < COLLECTION_MAX_SIZE:
        collection_name.insert_many(documents,False,False)
        count += 1 

