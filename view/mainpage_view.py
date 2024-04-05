import justpy as jp

from component.color import Color
import main

def MainPageView():
    color = Color()
    wp = jp.WebPage()
    wp.add(jp.P(text='메인페이지', classes='text-5xl m-2'))
    link = jp.A(text='Go back home', href='/signin', classes='text-lg hover:underline',  style=color.MainColor) #페이지 이동 얘시입니다 이거 보시고 하시면 됩니다.
    wp.add(link)
    return wp