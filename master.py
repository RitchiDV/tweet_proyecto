#python..
from uuid import UUID
from datetime import date
from typing import Optional
from datetime import datetime
#pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
#FAstapi
from fastapi import FastAPI,status


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
    burth_date:Optional[date] = Field(default=None)


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
@app.get(
   path= "/",
   status_code=status.HTTP_200_OK,
   tags=["home"]
    )
def home():
    return{"hello":"world"}
##users
@app.post(
    path="/signup",
    response_model=user,
    status_code=status.HTTP_201_CREATED,
    summary="registrer a user",
    tags=["Users"]
)
def signup ():
    pass

@app.post(
    path="/signup",
    response_model=user,
    status_code=status.HTTP_201_CREATED,
    summary="registrer a user",
    tags=["Users"]
)
def signup ():
    pass

@app.post(
    path="/signup",
    response_model=user,
    status_code=status.HTTP_201_CREATED,
    summary="registrer a user",
    tags=["Users"]
)
def signup ():
    pass

@app.post(
    path="/signup",
    response_model=user,
    status_code=status.HTTP_201_CREATED,
    summary="registrer a user",
    tags=["Users"]
)
def signup ():
    pass

@app.post(
    path="/signup",
    response_model=user,
    status_code=status.HTTP_201_CREATED,
    summary="registrer a user",
    tags=["Users"]
)
def signup ():
    pass