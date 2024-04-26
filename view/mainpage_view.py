from component.header import Header
import justpy as jp

from component.calendar import CalendarComponent

def MainPageView():
    head = Header("/")
    wp = jp.WebPage()
    head.show_header(wp)
    wp.add(jp.P(text='메인페이지', classes='text-5xl m-2'))

    link = jp.A(text='로그인 페이지 이동', href='/signin', classes='text-lg hover:underline',  ) #페이지 이동 얘시입니다 이거 보시고 하시면 됩니다.
    #link = jp.A(text='회원가입 페이지 이동', href='/signup', classes='text-lg hover:underline',  style=color.MainColor) #페이지 이동 얘시입니다 이거 보시고 하시면 됩니다.
    CalendarComponent().showCalendar(wp)
    wp.add(link)

    return wp