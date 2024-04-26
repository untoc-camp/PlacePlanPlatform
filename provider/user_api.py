import justpy as jp
async def Login(UserModel): 
    return await jp.get(f'login/{UserModel.id}/{UserModel.password}/{UserModel.name}')

