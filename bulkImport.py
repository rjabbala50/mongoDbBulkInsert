'''
... Description: This scripts bulk uploads documents to collections in mongodb
... @author Vrushali V
... @since September 15, 2021, 2.30 AM IST 
'''

COLLECTION_NAME   = "MyFirstDatabase"
CLUSTER_NAME      = "cluster0.gxrbo.mongodb.net"
MONGO_PREFIX      = "mongodb+srv"
DATABASE_NAME     = "My_shopping_list"
DATABASE_USERNAME = "m001-student"
DATABASE_PASSWORD = "m001-mongodb-basics"

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
    
    item_1 = {
            "item_Name": "Shopping",
            "discount":"100%",
            "price": 21000
            }
    item_2 = {
            "item_Name": "Shopping",
            "discount":"80%",
            "price": 2300
            }
    collection_name.insert_many([item_1,item_2])

    from dateutil import parser
    expiry_date = '2021-07-13T00:00:00.000Z'
    expiry = parser.parse(expiry_date)
    
    item_3 = {
            "item_Name": "Sporting",
            "quantity": 32,
            "price": 34,
            "expiry_date":expiry
            }
    collection_name.insert_one(item_3)
