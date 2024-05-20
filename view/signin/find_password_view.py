import justpy as jp

from element.header import Header

def FindPasswordView():
    wp = jp.WebPage()
    header = Header("/signin")
    header.show_header(wp)
    
    wp.add(jp.P(text='비밀번호 찾기', classes='text-5xl m-2'))
    return wp