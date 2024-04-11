import justpy as jp

from component.color import Color


def MainPageView():
    color = Color()
    wp = jp.WebPage()
    wp.add(jp.P(text='메인페이지', classes='text-5xl m-2'))
    link = jp.A(text='로그인 페이지 이동', href='/signin', classes='text-lg hover:underline',  style=color.MainColor) #페이지 이동 얘시입니다 이거 보시고 하시면 됩니다.
    link = jp.A(text='회원가입 페이지 이동', href='/signup', classes='text-lg hover:underline',  style=color.MainColor) #페이지 이동 얘시입니다 이거 보시고 하시면 됩니다.
    wp.add(link)
    return wp