import justpy as jp
from provider.api import api
async def Login(UserModel): 
    return await jp.get(f'{api.api}login/{UserModel.id}/{UserModel.password}/{UserModel.name}')

