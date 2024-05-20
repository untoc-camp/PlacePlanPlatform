import justpy as jp

from element.header import Header

def SignInView():
    wp = jp.WebPage()
    header = Header("/signin")
    header.show_header(wp)

    # Function to show the popup
    def show_popup(self, msg):
        # 팝업을 보이게 설정
        self.dialog.show = True
        self.dialog.set_class('flex')
        self.dialog.update()

    def close_popup(self, msg):
        # 팝업을 숨기게 설정
        self.dialog.show = False
        self.dialog.set_class('hidden')
        self.dialog.update()
    

    # 로그인 양식
    # 전체 화면을 중앙 정렬하기 위한 div
    main_div = jp.Div(classes="flex items-center justify-center min-h-screen", a=wp)

    # 로그인 양식을 담을 div
    login_form = jp.Div(classes="flex flex-col items-center justify-center bg-white p-8 w-96", a=main_div)
    login_text = jp.Div(text="Login", classes="text-5xl text-blue-500 font-semibold mb-4", a=login_form)
    blank_text = jp.Div(text="      ", classes="text-5xl")
    
    # Input 스타일 적용
    input_style = "border p-2 m-2 rounded-full w-full"
    username_input = jp.Input(placeholder="Username", a=login_form, classes=input_style)
    password_input = jp.Input(placeholder="Password", type="password", a=login_form, classes=input_style)
    
    dialog = jp.Div(classes="fixed inset-0 bg-gray-800 bg-opacity-50 items-center justify-center hidden", a=wp)
    dialog.show = False  # 처음에는 숨겨진 상태
    
    #비밀번호 찾기 링크
    find_password = jp.P(a=login_form, classes="w-full text-right")  # 부모 요소 설정
    find_password.add(jp.A(text="비밀번호 찾기", href="/signin/findPassword", classes="hover:underline text-xs pr-2"))

    # Button 스타일 적용
    button_style = "border p-2 m-2 rounded-full bg-blue-500 text-white w-full"
    login_button = jp.Button(text="로그인", a=login_form, classes=button_style)
    login_button.on('click', show_popup)  # Call show_popup function when button is clicked
    login_button.dialog = dialog

    # 팝업 내부 내용
    popup_content = jp.Div(classes="bg-white p-4 rounded-lg text-center", a=dialog)
    jp.P(text='아이디 또는 비밀번호가 일치하지 않습니다.', classes='my-5', a=popup_content)
    close_button = jp.Button(text='닫기', classes='bg-red-500 text-white p-2 rounded', a=popup_content, click=close_popup)
    close_button.dialog = dialog  # 닫기 버튼과 팝업 다이얼로그 연결

    jp.Br(a=login_form)
    
    # 회원가입 링크
    signup_text = jp.P(a=login_form)
    signup_text.text = "계정이 없으신가요? "
    signup_text.add(jp.A(text="회원가입", href="/signup", style="color: blue", classes="underline"))

    return wp