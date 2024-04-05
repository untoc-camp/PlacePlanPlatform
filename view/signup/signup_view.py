import justpy as jp

def SignupView():
    wp = jp.WebPage()
    wp.add(jp.P(text='회원가입 페이지', classes='text-5xl m-2'))
    return wp