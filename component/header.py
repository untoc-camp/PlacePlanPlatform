import justpy as jp

from component.color import MainColors
from component.font import Font
from model.user_model import UserModel, setUserModel

class Header:
    def __init__ (self, route):
        self.route = route
    
    def _nonMemberHeaderShow(self, wp):
        div = jp.Div(classes='flex h-16 bg-white shadow justify-between')
        header_left = jp.Div(classes='flex-1 flex items-center')
        text1_div = jp.Div(text="Text 1", classes="text-lg")
        text2_div = jp.Div(text="Text 2", classes="text-lg ml-4")
        text3_div = jp.Div(text="Text 3", classes="text-lg ml-4")

        header_left.add(text1_div, text2_div, text3_div)

        header_right = jp.Div(classes='flex-1 flex items-center justify-end')
        text1_div = jp.Div(text="Text 1", classes="text-lg")
        text2_div = jp.Div(text="Text 2", classes="text-lg")
        text3_div = jp.Div(text="Text 3", classes="text-lg")

        header_right.add(text1_div, text2_div, text3_div)

        div.add(header_left, header_right)

        wp.add(div)
    def _userMember(self, wp):
        pass

    def show_header(self, wp):
        self.user = UserModel(
            {"user_id": "", "user_name": "test", "user_password": "test"}
        )
        if self.user.user_id == "":
            self._nonMemberHeaderShow(wp)
            
        else:
            self._userMember(wp)