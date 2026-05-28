from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app=FastAPI()
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Specific function for getting loc ########

def autocomplete(q:str):
    url="https://atlas.mapmyindia.com/api/places/search/json"

    payload={
        "access_token":"YOUR_ACCESS_KEY",
        "region":"IND",
        "query":q,
        "location":"9.925557164854263, 76.35675339482806"
            }

    return requests.get(url,params=payload).json()



############################



@app.get("/geo")
def get_location(q:str):
    return autocomplete(q)