import justpy as jp

def SignInView():
    wp = jp.WebPage()
    wp.add(jp.P(text='로그인 페이지', classes='text-5xl m-2'))
    return wp