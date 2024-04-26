import provider.user_api as userApi
import model.user_model as userModel
def _getUserModel(json):
    userModel.setUserModel(json)

async def login(userModel):
    try : 
        res = await userApi.login(userModel)
        _getUserModel(res)
    except:
        pass