import justpy as jp
from element.header import Header

# 전역 변수로 시간 선택을 추적
selected_times = {
    day: {f"{hour:02d}:00": 0 for hour in range(9, 22)}
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
}

# 사용자 3명이 모두 오후 6시부터 8시까지 선택한 경우 반영
for day in selected_times:
    for hour in range(18, 20):  # 18시부터 20시까지
        time = f"{hour:02d}:00"
        selected_times[day][time] = 3

# 색상 설정 함수
def get_color(count):
    if count == 0:
        return "white"
    elif count == 1:
        return "lightblue"
    elif count == 2:
        return "blue"
    else:
        return "darkblue"

# 테이블 업데이트 함수
def TimePromiseDetailView():
    wp = jp.WebPage()
    header = Header("/timepromise/{time_promise_id}")
    header.show_header(wp)
    
    table = jp.Table(a=wp, classes="q-table", style="margin-top: 200px; margin-left: 50px")
    thead = jp.Thead(a=table)
    tr = jp.Tr(a=thead)
    
    # 테이블 헤더 - 요일
    jp.Th(a=tr, text="    ")
    for day in selected_times.keys():
        jp.Th(a=tr, text=day)
    
     # 테이블 본문 - 시간 슬롯 및 색상
    tbody = jp.Tbody(a=table)
    for hour in range(9, 22):
        tr = jp.Tr(a=tbody)
        jp.Td(a=tr, text=f"{hour:02d}:00", style="border: none;")  # 시간 열
        for day in selected_times:
            time = f"{hour:02d}:00"
            border_style = "border: 1px solid black;" if hour > 9 else "border: none;"
            jp.Td(a=tr, style=f"background-color: {get_color(selected_times[day][time])}; color: white; border: 1px solid black;")
    
    # 헤더의 테두리 설정 (1행 제외)
    
    return wp

