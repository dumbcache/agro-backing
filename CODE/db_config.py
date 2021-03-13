import json

def config():
    with open('db_user.json','r') as f:
        details=json.load(f)
    return(details)  
       