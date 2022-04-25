#python..
import json
from uuid import UUID
from datetime import date
from typing import Optional,List
from datetime import datetime
#pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
#FAstapi
from fastapi import FastAPI,status,Body


app=FastAPI()

#models = modelos
class userBase(BaseModel):
     user_id: UUID = Field(...)
     email: EmailStr= Field(...)


class userLogin(userBase):   
    password: str = Field(...,
    min_length=8,
    max_length=20
    )
    

class user(userBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date:Optional[date] = Field(default=None)

class userRegister(user):
     password: str = Field(...,
    min_length=8,
    max_length=20
    )


class tweet(BaseModel):
    tweet_id: UUID
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
        )
    created_at: datetime =Field(default=datetime.now())
    update_at:Optional[datetime] =Field(default=None)
    by: user = Field(...)

#path operations
#_____________________________________________________________
##users
###registrar usuario
@app.post(
    path="/signup",
    response_model=user,
    status_code=status.HTTP_201_CREATED,
    summary="registrer a user",
    tags=["Users"]
)
def signup (user: userRegister = Body(...)):

    """
    signup a user

    this path operation registrer a user in the app 
    parameters:
        - REQUEST BODY PARAMETERS
            - user: userRegister

    Returns a json with the basic user information:
        - user_id: UUID
        - email: Emailstr
        - first_name : str
        - last_name: str
        - birth date: datetime

    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict =user.dict()
        user_dict["user_id"]=str (user_dict["user_id"])
        user_dict["birth_date"]=str (user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user



###login users
@app.post(
    path="/login",
    response_model=user,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
)
def login ():
    pass
###show all users
@app.get(
    path="/users",
    response_model=List[user],
    status_code=status.HTTP_200_OK,
    summary="show a users",
    tags=["Users"]
)
def show_all_users():
    """
    this path operation shows all users in the app

    parameters:
        -
    returns a json list whit all users in the app, with the following keys:
        - user_id: UUID
        - email: Emailstr
        - first_name : str
        - last_name: str
        - birth date: datetime
    """
    with open ("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results
### show a user
@app.get(
    path="/users/{user_id}",
    response_model=user,
    status_code=status.HTTP_200_OK,
    summary="show a spesific user information",
    tags=["Users"]
)
def show_a_user ():
    pass
### delete a user
@app.delete(
    path="/user/{user_id}/delete",
    response_model=user,
    status_code=status.HTTP_200_OK,
    summary="delete a user",
    tags=["Users"]
)
def delete_a_user ():
    pass
###update a user
@app.put(
    path="/user/{user_id}/update",
    response_model=user,
    status_code=status.HTTP_200_OK,
    summary="update a user",
    tags=["Users"]
)
def update_a_user ():
    pass


##_____________________________________________
##tweet

##tweet
###show all tweets
@app.get(
   path= "/",
   response_model=List[tweet],
   status_code=status.HTTP_200_OK,
   summary="show all tweets",
   tags=["tweets"]
    )
def home():
    return{"hello":"world"}
###post a tweet
@app.post(
    path="/post",
    response_model=tweet,
    status_code=status.HTTP_201_CREATED,
    summary="post a tweet",
    tags=["tweets"]
)
def post ():
    pass
###show a tweet
@app.get(
    path="/tweet/{tweet_id}",
    response_model=tweet,
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["tweets"]
)
def show_a_tweet ():
    pass
### delete a tweet
@app.delete(
    path="/tweet/{tweet_id}/delete",
    response_model=tweet,
    status_code=status.HTTP_200_OK,
    summary="delete a tweet",
    tags=["tweets"]
)
def delete_a_user ():
    pass
### update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=tweet,
    status_code=status.HTTP_200_OK,
    summary="update a tweet",
    tags=["tweets"]
)
def update_a_tweet():
    pass
