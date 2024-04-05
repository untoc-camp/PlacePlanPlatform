import justpy as jp


def MainPageView():
    wp = jp.WebPage()
    wp.add(jp.P(text='메인페이지', classes='text-5xl m-2'))
    link = jp.A(text='Go back home', href='/signin', classes='text-lg text-blue-500 hover:underline') #페이지 이동 얘시입니다 이거 보시고 하시면 됩니다.
    wp.add(link)
    return wp