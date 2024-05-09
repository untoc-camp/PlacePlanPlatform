import justpy as jp

from element.color import MainColors
from element.font import Font
from model.user_model import UserModel, getUserModel, setUserModel

class Header:
    def __init__ (self, route):
        self.route = route
        self.font = Font()
        self.color = MainColors()
    
    def _nonMemberHeaderShow(self, wp):
        div = jp.Div(classes='flex h-16 bg-white shadow justify-between')
        header_left = jp.Div(classes='flex-1 flex items-center')

        bottom_blue_retengle = jp.Div(classes='h-1 w-full mt-1', style = f'background-color: {self.color.MainColor}')
        bottom_white_retengle = jp.Div(classes='h-1 w-full mt-1', style = f'background-color: white')

        main_logo_img = jp.Img(src='https://www.python.org/static/community_logos/python-powered-h-140x182.png', classes = "ml-4", style='height: 50px; width: auto;')
        main_page_a = jp.A(text="메인 화면", classes=self.font.Heading4_Bold + " ml-8 mt-4", href = "/", style = f'color: {self.color.TextColor}')
        main_page_a.add(bottom_blue_retengle if self.route == "/" else bottom_white_retengle)

        introduce_div = jp.A(text="시간 약속", classes=self.font.Heading4_Bold + " ml-8 mt-4", href = "/signin", style = f'color: {self.color.TextColor}')
        introduce_div.add(bottom_blue_retengle if self.route == "/timepromise" else bottom_white_retengle)


        header_left.add(main_logo_img, main_page_a, introduce_div)

        header_right = jp.Div(classes='flex-1 flex items-center justify-end')
        login_a = jp.A(text = "로그인", classes = self.font.Heading4_Bold + " mr-8 mt-4", href = "/signin", style = f'color: {self.color.TextColor}')
        login_a.add(bottom_blue_retengle if self.route[:7] == "/signin" else bottom_white_retengle)

        signup_a = jp.A(text= "회원 가입", classes = self.font.Heading4_Bold + " mr-4 mt-4", href = "/signup", style = f'color: {self.color.TextColor}')
        signup_a.add(bottom_blue_retengle if self.route[:7] == "/signup" else bottom_white_retengle)
        
        header_right.add(login_a, signup_a)

        div.add(header_left, header_right)

        wp.add(div)
        
        
    def _userMember(self, wp): #로그인 시 유저 화면
        user = getUserModel()
        div = jp.Div(classes='flex h-16 bg-white shadow justify-between')
        header_left = jp.Div(classes='flex-1 flex items-center')

        bottom_blue_retengle = jp.Div(classes='h-1 w-full mt-1', style = f'background-color: {self.color.MainColor}')
        bottom_white_retengle = jp.Div(classes='h-1 w-full mt-1', style = f'background-color: white')

        main_logo_img = jp.Img(src='https://www.python.org/static/community_logos/python-powered-h-140x182.png', classes = "ml-4", style='height: 50px; width: auto;')
        main_page_a = jp.A(text="시간 약속", classes=self.font.Heading4_Bold + " ml-8 mt-4", href = "/timepromise", style = f'color: {self.color.TextColor}')
        main_page_a.add(bottom_blue_retengle if self.route == "/timeprimse" else bottom_white_retengle)

        introduce_div = jp.A(text="약속 만들기", classes=self.font.Heading4_Bold + " ml-8 mt-4", href = "/timepromise/make", style = f'color: {self.color.TextColor}')
        introduce_div.add(bottom_blue_retengle if self.route == "/timepromise/make" else bottom_white_retengle)


        header_left.add(main_logo_img, main_page_a, introduce_div)

        header_right = jp.Div(classes='flex-1 flex items-center justify-end')
        login_a = jp.A(text = "로그인", classes = self.font.Heading4_Bold + " mr-8 mt-4", href = "/signin", style = f'color: {self.color.TextColor}')
        login_a.add(bottom_blue_retengle if self.route[:7] == "/signin" else bottom_white_retengle)

        signup_a = jp.A(text= "회원 가입", classes = self.font.Heading4_Bold + " mr-4 mt-4", href = "/signup", style = f'color: {self.color.TextColor}')
        signup_a.add(bottom_blue_retengle if self.route[:7] == "/signup" else bottom_white_retengle)
        
        header_right.add(login_a, signup_a)

        div.add(header_left, header_right)

        wp.add(div)
        

    def show_header(self, wp):
        self.user = UserModel(
            {"user_id": "test1234", "user_name": "name", "user_password": "test"}
        )
        if self.user== None:
            self._nonMemberHeaderShow(wp)
            
        else:
            self._userMember(wp)
        
