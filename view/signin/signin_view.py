import justpy as jp

from element.header import Header

def SignInView():
    wp = jp.WebPage()
    header = Header("/signin")
    header.show_header(wp)
    wp.add(jp.P(text='로그인 페이지', classes='text-5xl m-2'))
    return wp