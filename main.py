import justpy as jp
from starlette.responses import HTMLResponse


from element.color import MainColors
from route.route import route
from view.mainpage_view import MainPageView

route()

def setup():
    jp.SetRoute("/")  # 홈 페이지 정의    
    jp.justpy(MainPageView)
    
jp.justpy(setup)    

