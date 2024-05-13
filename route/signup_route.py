import justpy as jp

from view.signup.email_confirm_view import EmailConfirmView
from view.signup.signup_view import SignUpView

def SignUpRoute():
    jp.Route('/signup', SignUpView)
    jp.Route('/signup/findId', EmailConfirmView)