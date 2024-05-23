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
        selected_times[day][time] = 2

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
    
    # 색상 설명 테이블 추가
    color_table = jp.Table(a=wp, classes="q-table", style="margin-top: 150px; margin-left: 90px; border-collapse: collapse;")
    color_tbody = jp.Tbody(a=color_table)
    color_tr = jp.Tr(a=color_tbody)
    
    # 색상 설명 행
    color_info = [
        {"count": 0, "color": "white"},
        {"count": 1, "color": "lightblue"},
        {"count": 2, "color": "blue"}
    ]
    
    for info in color_info:
        jp.Td(a=color_tr, text=f"{info['count']} users", style=f"background-color: {info['color']}; color: black; border: 1px solid black; text-align: center; padding: 10px;")

    # 메인 테이블 추가
    table = jp.Table(a=wp, classes="q-table", style="margin-top: 20px; margin-left: 50px; border-collapse: collapse;")
    thead = jp.Thead(a=table)
    tr = jp.Tr(a=thead)
    
    # 테이블 헤더 - 요일
    jp.Th(a=tr, text="    ", style="border: none;")
    for day in selected_times.keys():
        jp.Th(a=tr, text=day, style="border: none;")
    
     # 테이블 본문 - 시간 슬롯 및 색상
    tbody = jp.Tbody(a=table)
    for hour in range(9, 22):
        tr = jp.Tr(a=tbody)
        jp.Td(a=tr, text=f"{hour:02d}:00", style="border: none;")  # 시간 열
        for day in selected_times:
            time = f"{hour:02d}:00"
            jp.Td(a=tr, style=f"background-color: {get_color(selected_times[day][time])}; color: white; border: 1px solid black;")
    
    return wp