import justpy as jp

from element.header import Header

def validate_passwords(self, msg):
    password = msg.page.password_input.value
    password_check = msg.page.password_check_input.value
    error_message = msg.page.error_message

    if password != password_check:
        msg.page.password_input.set_class('border-red-500')
        msg.page.password_check_input.set_class('border-red-500')
        error_message.text = "비밀번호가 일치하지 않습니다"
        error_message.set_class('text-red-500 text-sm') # 적용안됨
    else:
        msg.page.password_input.set_class('border-green-500')
        msg.page.password_check_input.set_class('border-green-500')
        error_message.text = ""
        
def SignUpView():
    wp = jp.WebPage()
    header = Header("/signup")
    header.show_header(wp)
    
    # 회원가입 양식
    # 전체 화면을 중앙 정렬하기 위한 div
    main_div = jp.Div(classes="flex items-center justify-center min-h-screen", a=wp)

    # 회원가입 양식을 담을 div
    signup_form = jp.Div(classes="flex flex-col items-center justify-center bg-white p-8 w-96", a=main_div)
    signup_text = jp.Div(text="Sign Up", classes="text-5xl text-blue-500 font-semibold mb-4", a=signup_form)
    
    # Input 스타일 적용
    input_style = "border p-2 m-2 rounded-full w-full"
    username_input = jp.Input(placeholder="이름", a=signup_form, classes=input_style)
    id_input = jp.Input(placeholder="UntocPPP@pusan.ac.kr", a=signup_form, classes=input_style)
    password_input = jp.Input(placeholder="Password", type="password", a=signup_form, classes=input_style)
    password_check_input = jp.Input(placeholder="Password", type="password", a=signup_form, classes=input_style)
    
     # Error message div
    error_message = jp.Div(classes="text-red-500 mt-2", a=signup_form)
    
    # Button 스타일 적용
    button_style = "border p-2 m-2 rounded-full bg-blue-500 text-white w-full"
    signup_button = jp.Button(text="회원가입", a=signup_form, classes=button_style)
    
    # Store the password inputs and error message in the page for access in the event handler
    wp.password_input = password_input
    wp.password_check_input = password_check_input
    wp.error_message = error_message
    
    # Add the event handler to the button
    signup_button.on('click', validate_passwords)

    return wp