import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://mongodbproject2account:uu4pHNlMGGmS4F31WXNWrRG9agrxynfak4Tu4HQMd5t5pAM1VbXf1SOIpOhiUWZ1ZpvKbGxVMCJcwJZm7qdW2w==@mongodbproject2account.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@mongodbproject2account@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['project2mongodb']
            collection = database['advertisements']
            
            query = {'_id': id}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
