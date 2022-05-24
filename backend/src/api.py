from .models import user
from fastapi import FastAPI, Request,HTTPException
import requests
import json 
from fastapi.middleware.cors import CORSMiddleware
import logging


#init fastapi app
app = FastAPI()
logger = logging.getLogger(__name__)
logging.basicConfig(filename='application.log',level=logging.DEBUG)

#in order to make cross origin requests from the frontend to back we need to configure the origin details.
origins = [
    'http://localhost:3000',
    'localhost:3000'
]


#add the middle ware layer, using CORS, and the origins we just described above.
app.add_middleware(CORSMiddleware,allow_origins=origins)

#gets the specific details of a user using the reqres API.
def get_user_details(user_id):
    func_response = ""
    #try call the api and get repsonse.
    try:
        url = f"https://reqres.in/api/users/{user_id}"
        response = requests.get(url)
    except HTTPException as exc:
        logger.exception(exc)
        raise HTTPException(status_code=500,detail="Failed to contact users API.")

    if response != "":
        #if we have a repsonse then check it is valid.
        if response.status_code == 404:
            raise HTTPException(status_code=404,detail="User does not exist!")
        func_response = response.text        
    return func_response

#function containst the reqres api to get all users. 
def get_all_users():
    try:
        url = f"https://reqres.in/api/users?page=2"
        response = requests.get(url)
        
        #create a json payload to enable processing of the data
        payload = json.loads(response.text)

        users = []
        #the response has a data payloaf formatted as a dictionary.
        for user in payload['data']:
            users.append({"id":user['id'],"name":user['first_name']})

        #return back a list of users
        return users
    except Exception as exc:
        logger.exception(exc)
        return ""

#home route
@app.get("/")
async def read_root(request: Request) -> dict:
    all_users = get_all_users()
    #if all users comes back as an empty string instead of a dict, then raise an error
    if all_users == "":
        raise HTTPException(status_code=400,detail="Failed to get users from host API.")

    return all_users

@app.get("/user/")
async def read_user(user_id: int =0) -> dict:
    print(user_id)
    
    #contacts API and returns user details if found. Also raises HTTP EXCEPTION
    payload = get_user_details(user_id)

    #try process the payload data
    try:
        json_data = json.loads(payload)
        #feeds the data part of the JSON obj into the User pydantic model.
        new_user = user.User(**json_data['data'])
    except Exception as exc:
        logger.exception(exc)
        raise HTTPException(status_code=500,detail=exc)

    #return user details to the caller
    return new_user