import justpy as jp

from route.signin_route import SignInRoute
from route.signup_route import SignUpRoute
from route.time_promise_route import TimePromiseRoute
from view.mainpage_view import MainPageView



def route():
    jp.Route('/', MainPageView)
    SignInRoute()
    SignUpRoute()
    TimePromiseRoute()