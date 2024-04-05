import justpy as jp

from view.signin.find_password_view import FindPasswordView
from view.signin.signin_view import SignInView

def SignInRoute():
    jp.Route('/signin', SignInView)
    jp.Route('/signin/findPassword', FindPasswordView)