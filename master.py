#FAstapi
from fastapi import FastAPI,status


app=FastAPI()


@app.get(
   path= "/",
   status_code=status.HTTP_200_OK,
   tags=["home"]
    )
def home():
    return{"hello:world"}