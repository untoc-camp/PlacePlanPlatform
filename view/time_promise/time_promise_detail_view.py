import justpy as jp
from element.header import Header
import datetime
import json

# JSON 형식의 사용자 선택 데이터 (예제 데이터)
json_data = '''
{
    "Mon": {
        "09:00": ["user1"], "10:00": [], "11:00": [], "12:00": [], "13:00": [], "14:00": [], "15:00": [], "16:00": [], "17:00": [], "18:00": ["user1", "user2", "user3"], "19:00": ["user1", "user2", "user3"], "20:00": [], "21:00": []
    },
    "Tue": {
        "09:00": [], "10:00": [], "11:00": [], "12:00": [], "13:00": [], "14:00": [], "15:00": [], "16:00": [], "17:00": [], "18:00": ["user1", "user2", "user3"], "19:00": ["user1", "user2", "user3"], "20:00": [], "21:00": []
    },
    "Wed": {
        "09:00": [], "10:00": [], "11:00": [], "12:00": [], "13:00": [], "14:00": [], "15:00": [], "16:00": [], "17:00": [], "18:00": ["user1", "user2", "user3"], "19:00": ["user1", "user2", "user3"], "20:00": [], "21:00": []
    },
    "Thu": {
        "09:00": [], "10:00": [], "11:00": [], "12:00": [], "13:00": [], "14:00": [], "15:00": [], "16:00": [], "17:00": [], "18:00": ["user1", "user2", "user3"], "19:00": ["user1", "user2", "user3"], "20:00": [], "21:00": []
    },
    "Fri": {
        "09:00": [], "10:00": [], "11:00": [], "12:00": [], "13:00": [], "14:00": [], "15:00": [], "16:00": [], "17:00": [], "18:00": ["user1", "user2", "user3"], "19:00": ["user1", "user2", "user3"], "20:00": [], "21:00": []
    },
    "Sat": {
        "09:00": [], "10:00": [], "11:00": [], "12:00": [], "13:00": [], "14:00": [], "15:00": [], "16:00": [], "17:00": [], "18:00": ["user1", "user2", "user3"], "19:00": ["user1", "user2", "user3"], "20:00": [], "21:00": []
    },
    "Sun": {
        "09:00": [], "10:00": [], "11:00": [], "12:00": [], "13:00": [], "14:00": [], "15:00": [], "16:00": [], "17:00": [], "18:00": ["user1", "user2", "user3"], "19:00": ["user1", "user2", "user3"], "20:00": [], "21:00": []
    }
}
'''

# JSON 데이터를 파싱하여 selected_times 초기화
selected_times = json.loads(json_data)

with open('data/location.json', 'r', encoding='utf-8') as file:
        location_data = json.load(file)[0]

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

def TimePromiseDetailView():
    wp = jp.WebPage()
    header = Header("/timepromise/{time_promise_id}")
    header.show_header(wp)
    
    headerline = jp.Div(a=wp, text=location_data["title"], style="color: gray; font-size: 26px; font-weight: bold; margin-top: 30px; margin-left:30px")
    sub_header = jp.Div(a=wp, text=f'주최자: {location_data["organizer"]}', style="color: gray; font-size: 20px; font-weight: bold; margin-left:30px")
    sub_sub_header = jp.Div(a=wp, text=f'약속 종류: {location_data["promise_type"]}', style="color: gray; font-size: 20px; font-weight: bold; margin-left:30px")
    
    
    # 전체 컨테이너
    container = jp.Div(a=wp, classes="flex flex-col justify-start", style="margin-top: 50px; margin-left: 30px;")
    
    # 색상 설명 테이블 추가
    color_table = jp.Table(a=container, classes="q-table", style="margin-bottom: 20px; border-collapse: collapse; width: 25%;")
    color_tbody = jp.Tbody(a=color_table)
    color_tr = jp.Tr(a=color_tbody)
    
    # 색상 설명 행
    color_info = [
        {"count": 0, "color": "white"},
        {"count": 1, "color": "lightblue"},
        {"count": 2, "color": "blue"},
        {"count": 3, "color": "darkblue"}
    ]
    
    for info in color_info:
        jp.Td(a=color_tr, text=f"{info['count']} users", style=f"background-color: {info['color']}; color: black; border: 1px solid black; text-align: center; padding: 10px;")

    # 요일별 테이블들을 감싸는 컨테이너
    table = jp.Table(a=container, style="width:25%")
    headers = [" ", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    header_row = jp.Tr(a=table)

    for h in headers:
        # 첫 번째 행의 border를 없애는 스타일 적용
        jp.Th(a=header_row, text=h, style="border: none;")

    for hour in range(9, 22):
        row = jp.Tr(a=table)
        time_slot = f"{hour:02d}:00"
        # 첫 번째 열의 border를 없애는 스타일 적용
        jp.Td(a=row, text=time_slot, style="border: none;")
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            users = selected_times[day].get(time_slot, [])
            count = len(users)
            color = get_color(count)
            jp.Td(a=row, style=f"background-color: {color}; border: 1px solid black;")
            
    return wp