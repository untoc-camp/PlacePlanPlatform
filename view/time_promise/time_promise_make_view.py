import justpy as jp

def TimePromiseMakeView():
    wp = jp.WebPage()
    wp.add(jp.P(text='시간 약속 만들기 페이지', classes='text-5xl m-2'))
    return wp