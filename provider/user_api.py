import justpy as jp
from static.api import api
import requests, json

async def Login(UserModel): 
    response = requests.get(f'{api.api}login')
    if response.status_code == 200:
        
        return response.json()
    else:
        return []
    

# response = requests.post(URL, data=data)
# response = requests.post(URL, data=json.dumps(data))