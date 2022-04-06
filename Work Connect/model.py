import pymongo
import os

client = pymongo.MongoClient("mongodb+srv://admin:"+os.environ.get('CS_Password')+"@cluster0.knoxq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.ProjectDB
# db.create_collection('Jobs')
jobsDB = db.companies

# jobsDB.insert_one(
#     {"company_name": "Company X", "job_scope": {"tech": "www.tech.com", "business": "www.business.com", "finance": "www.finance.com"}}
# )

# a = jobsDB.find_one({"job_scope.tech": {"$exists": 1}}) #syntax to check if the inner field "tech" exists in "job_scope" field
# print(a) 