import justpy as jp

def EmailConfirmView():
    wp = jp.WebPage()
    wp.add(jp.P(text='이메일 인증 페이지', classes='text-5xl m-2'))
    return wp