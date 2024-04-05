import justpy as jp

from view.signup.email_confirm_view import EmailConfirmView
from view.signup.signup_view import SignupView

def SignUpRoute():
    jp.Route('/signup', SignupView)
    jp.Route('/signup/findId', EmailConfirmView)