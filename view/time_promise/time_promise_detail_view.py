import justpy as jp

def TimePromiseDetailView():
    wp = jp.WebPage()
    wp.add(jp.P(text='시간약속상세페이지', classes='text-5xl m-2'))
    return wp