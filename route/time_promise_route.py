import justpy as jp

from view.time_promise.time_promise_detail_view import TimePromiseDetailView
from view.time_promise.time_promise_main_view import TimePromiseMainView

def TimePromiseRoute():
    jp.Route('/timePromise', TimePromiseMainView)
    jp.Route('/timePromise/{time_promise_id}', TimePromiseDetailView)
    