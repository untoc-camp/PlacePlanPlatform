import justpy as jp

from element.header import Header

def SignupView():
    wp = jp.WebPage()
    header = Header("/signup")
    header.show_header(wp)
    wp.add(jp.P(text='회원가입 페이지', classes='text-5xl m-2'))
    return wp