import justpy as jp

from view.time_promise.time_promise_view import TimePromiseView

def TimePromiseRoute():
    jp.Route('/timePromise', TimePromiseView)
    