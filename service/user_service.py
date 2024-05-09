import provider.user_api as userApi
import model.user_model as userModel
def __getUserModel(json):
    userModel.setUserModel(json)

async def login(userModel):
    try : 
        res = await userApi.login(userModel)
        __getUserModel(res)
    except:
        pass