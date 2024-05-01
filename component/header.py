import justpy as jp

from component.color import MainColors
from component.font import Font
from model.user_model import UserModel, setUserModel

class Header:
    def __init__ (self, route):
        self.route = route
        self.font = Font()
        self.color = MainColors()
    
    def _nonMemberHeaderShow(self, wp):
        div = jp.Div(classes='flex h-16 bg-white shadow justify-between')
        header_left = jp.Div(classes='flex-1 flex items-center')

        bottom_retengle = jp.Div(classes='h-1 w-full mt-1', style = f'background-color: {self.color.MainColor}')
        text1_div = jp.Img(src='https://www.python.org/static/community_logos/python-powered-h-140x182.png', style='height: 50px; width: auto;')
        text2_div = jp.Div(text="메인 화면", classes=self.font.Heading4_Bold + " ml-4 mt-4", style = f'color: {self.color.TextColor}')
        text2_div.add(bottom_retengle)
        text3_div = jp.Div(text="PPP 소개", classes=self.font.Heading4_Bold + " ml-4 mt-4", style = f'color: {self.color.TextColor}')


        header_left.add(text1_div, text2_div, text3_div)

        header_right = jp.Div(classes='flex-1 flex items-center justify-end')
        text1_div = jp.Div(text="Text 1", classes= "text-lg")
        text2_div = jp.Div(text="Text 2", classes= "text-lg")
        text3_div = jp.Div(text="Text 3", classes= "text-lg")

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