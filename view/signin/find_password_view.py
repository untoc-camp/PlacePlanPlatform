import justpy as jp

def FindPasswordView():
    wp = jp.WebPage()
    wp.add(jp.P(text='비밀번호 찾기', classes='text-5xl m-2'))
    return wp