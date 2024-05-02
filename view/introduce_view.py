import justpy as jp

from element.header import Header

def IntroduceView():
    wp = jp.WebPage()
    head = Header("/introduce")
    head.show_header(wp)
    wp.add(jp.P(text='소개 페이지', classes='text-5xl m-2'))
    return wp