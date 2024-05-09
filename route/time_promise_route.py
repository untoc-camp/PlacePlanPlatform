import justpy as jp

from view.time_promise.time_promise_detail_view import TimePromiseDetailView
from view.time_promise.time_promise_main_view import TimePromiseMainView
from view.time_promise.time_promise_make_view import TimePromiseMakeView

def TimePromiseRoute():
    jp.Route('/timepromise', TimePromiseMainView)
    jp.Route('/timepromise/{time_promise_id}', TimePromiseDetailView)
    jp.Route('/timepromise/make', TimePromiseMakeView)
    