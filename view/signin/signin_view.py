import justpy as jp

from element.header import Header

def SignInView():
    wp = jp.WebPage()
    header = Header("/signin")
    header.show_header(wp)

    jp.P(text='로그인 페이지', classes='text-5xl m-2', a=wp)
    
    # 로그인 양식
    login_form = jp.Div(classes="flex flex-col items-center justify-center")
    
    # Input 스타일 적용
    input_style = "border p-2 m-2 rounded-full"
    username_input = jp.Input(placeholder="Username", a=login_form, classes=input_style)
    password_input = jp.Input(placeholder="Password", type="password", a=login_form, classes=input_style)
    
     # 비밀번호 찾기 링크
    find_password_link = jp.A(text="비밀번호 찾기", href="/signin/findpassword", a=login_form, classes="text-xs hover:underline")
    find_password_link.style = "margin-top: 2px; margin-right: 10px;"  # 간격 설정

    
    # Button 스타일 적용
    button_style = "border p-2 m-2 rounded-full bg-blue-500 text-white"
    login_button = jp.Button(text="로그인", a=login_form, classes=button_style)

    
    jp.Br(a=login_form)
    
    # 회원가입 링크
    signup_text = jp.P(a=login_form)
    signup_text.text = "계정이 없으신가요? "
    signup_text.add(jp.A(text="회원가입 하기", href="/signup", classes="hover:underline"))


    wp.add(login_form)

    return wp

jp.justpy(SignInView)