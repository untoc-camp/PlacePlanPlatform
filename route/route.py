import justpy as jp
import re

from starlette.responses import HTMLResponse

from route.signin_route import SignInRoute
from route.signup_route import SignUpRoute
from route.time_promise_route import TimePromiseRoute
from view.introduce_view import IntroduceView
from view.mainpage_view import MainPageView




def route():
    jp.Route('/', MainPageView)
    jp.Route('/introduce', IntroduceView)
    SignInRoute()
    SignUpRoute()
    TimePromiseRoute()
