import pymongo
import os

client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ.get('CS_Password')+"@cluster0.knoxq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.ProjectDB
# db.create_collection('Jobs')
jobsDB = db.companies
