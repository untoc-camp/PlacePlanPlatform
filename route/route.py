import justpy as jp
import re

from starlette.responses import HTMLResponse
from view.mainpage_view import MainPageView
from route.signin_route import SignInRoute
from route.signup_route import SignUpRoute
from route.time_promise_route import TimePromiseRoute





def route():
    jp.Route('/', MainPageView)
    SignInRoute()
    SignUpRoute()
    TimePromiseRoute()
