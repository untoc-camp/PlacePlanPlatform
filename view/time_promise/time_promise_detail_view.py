import justpy as jp
from element.header import Header
import json
from datetime import datetime, timedelta

# JSON 파일에서 데이터를 읽어오는 함수
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# JSON 파일 경로
json_file_path = 'data/schedule.json'

# JSON 데이터를 파일에서 불러와서 초기화
data = load_json_data(json_file_path)
selected_times = data['schedule']
dates = list(selected_times.keys())
date_index = 0  # 현재 날짜 범위의 시작 인덱스

# 사용자가 선택한 시간을 저장할 딕셔너리
user_selected_times = {}

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

def update_table(dates_to_show, table, time_slots):
    table.delete_components()
    header_row = jp.Tr(a=table)
    headers = [" "] + [datetime.strptime(date.split()[0], '%Y.%m.%d').strftime('%m/%d') + " " + date.split()[1] for date in dates_to_show]
    for h in headers:
        jp.Th(a=header_row, text=h, style="border: none; padding: 10px; text-align: center; color: #5C5F64;")

    for hour in range(9, 22):
        row = jp.Tr(a=table)
        time_slot = f"{hour:02d}:00"
        jp.Td(a=row, text=time_slot, style="border: none; padding: 10px; text-align: center; color: #5C5F64;")
        
        for date in dates_to_show:
            users = time_slots.get(date, {}).get(time_slot, [])
            count = len(users)
            color = get_color(count)
            jp.Td(a=row, style=f"background-color: {color}; border: 1px solid black; padding: 10px;", text=" ".join(users) if users else "No users")

def move_left(self, msg):
    global date_index
    if date_index > 0:
        date_index -= 7
        dates_to_show = dates[date_index:date_index + 7]
        update_table(dates_to_show, self.table, self.time_slots)
        update_date_range(dates_to_show, self.date_range)

def move_right(self, msg):
    global date_index
    if date_index + 7 < len(dates):
        date_index += 7
        dates_to_show = dates[date_index:date_index + 7]
        update_table(dates_to_show, self.table, self.time_slots)
        update_date_range(dates_to_show, self.date_range)

def update_date_range(dates_to_show, date_range):
    start_date = datetime.strptime(dates_to_show[0].split()[0], '%Y.%m.%d').strftime('%m/%d')
    start_day = dates_to_show[0].split()[1]
    end_date = datetime.strptime(dates_to_show[-1].split()[0], '%Y.%m.%d').strftime('%m/%d')
    end_day = dates_to_show[-1].split()[1]
    date_range.text = f"{start_date} ({start_day}) ~ {end_date} ({end_day})"

def get_common_available_times(time_slots, all_users):
    common_times = {}
    for date, slots in time_slots.items():
        for time, users in slots.items():
            if set(users) == set(all_users):
                if date not in common_times:
                    common_times[date] = []
                common_times[date].append(time)
    return common_times

def format_time_range(times):
    if not times:
        return ""
    
    times.sort()
    time_ranges = []
    current_start = datetime.strptime(times[0], '%H:%M')
    current_end = current_start + timedelta(hours=1)
    
    for time in times[1:]:
        next_time = datetime.strptime(time, '%H:%M')
        if next_time == current_end:
            current_end += timedelta(hours=1)
        else:
            time_ranges.append(f"{current_start.strftime('%H:%M')} ~ {current_end.strftime('%H:%M')}")
            current_start = next_time
            current_end = current_start + timedelta(hours=1)
    
    time_ranges.append(f"{current_start.strftime('%H:%M')} ~ {current_end.strftime('%H:%M')}")
    return ", ".join(time_ranges)

def update_common_available_times(container_right, common_times):
    container_right.delete_components()
    if not common_times:
        jp.Div(a=container_right, text="모두가 가능한 시간이 없습니다.", style="margin-bottom: 10px; color: #5C5F64; font-size: 18px;")
    else:
        for date, times in common_times.items():
            formatted_date = datetime.strptime(date.split()[0], '%Y.%m.%d').strftime('%m/%d')
            jp.Div(a=container_right, text=f"{formatted_date}", style="margin-bottom: 10px; color: #5C5F64; font-size: 18px; font-weight: bold;")
            time_range = format_time_range(times)
            jp.Div(a=container_right, text=f"{time_range}", style="margin-left: 10px; margin-bottom: 5px; color: #5C5F64; font-size: 16px;")

def time_select(self, msg):
    if self.style == "background-color: white; border: 1px solid black; padding: 10px;":
        self.style = "background-color: lightgreen; border: 1px solid black; padding: 10px;"
        self.selected = True
    else:
        self.style = "background-color: white; border: 1px solid black; padding: 10px;"
        self.selected = False

def show_select_table(self, msg):
    self.select_table.delete_components()
    dates_to_show = dates[date_index:date_index + 7]
    header_row = jp.Tr(a=self.select_table)
    headers = [" "] + [datetime.strptime(date.split()[0], '%Y.%m.%d').strftime('%m/%d') + " " + date.split()[1] for date in dates_to_show]
    for h in headers:
        jp.Th(a=header_row, text=h, style="border: none; padding: 10px; text-align: center; color: #5C5F64;")

    for hour in range(9, 22):
        row = jp.Tr(a=self.select_table)
        time_slot = f"{hour:02d}:00"
        jp.Td(a=row, text=time_slot, style="border: none; padding: 10px; text-align: center; color: #5C5F64;")
        
        for date in dates_to_show:
            cell = jp.Td(a=row, style="background-color: white; border: 1px solid black; padding: 10px;")
            cell.selected = False
            cell.date = date
            cell.time_slot = time_slot
            cell.on('click', time_select)

def apply_selected_times(self, msg):
    for row in self.select_table.components:
        if isinstance(row, jp.Tr):
            for cell in row.components:
                if isinstance(cell, jp.Td) and hasattr(cell, 'selected') and cell.selected:
                    date = cell.date
                    time_slot = cell.time_slot
                    if date not in selected_times:
                        selected_times[date] = {}
                    if time_slot not in selected_times[date]:
                        selected_times[date][time_slot] = []
                    selected_times[date][time_slot].append("user")  # 여기서 "user"는 사용자를 나타냅니다.

    dates_to_show = dates[:7]
    update_table(dates_to_show, self.table, selected_times)
    all_users = list(set().union(*[set(users) for users in selected_times.values()]))
    common_times = get_common_available_times(selected_times, all_users)
    update_common_available_times(self.container_right, common_times)

def TimePromiseDetailView():
    wp = jp.WebPage()
    header = Header("/timepromise/{time_promise_id}")
    header.show_header(wp)
    
    # 제목, 주최자, 약속 종류를 JSON 데이터에서 불러와서 표시
    headerline = jp.Div(a=wp, text=data['title'], style="color: #5C5F64; font-size: 30px; font-weight: bold; margin-top: 30px; margin-left:65px")
    sub_header = jp.Div(a=wp, text=f"주최자: {data['host']}", style="color: #5C5F64; font-size: 24px; font-weight: bold; margin-left:65px")
    sub_sub_header = jp.Div(a=wp, text=f"약속 종류: {data['type']}", style="color: #5C5F64; font-size: 24px; font-weight: bold; margin-left:65px")
    
    # 전체 컨테이너
    container = jp.Div(a=wp, classes="flex flex-row justify-start", style="margin-top: 50px; margin-left: 100px; gap: 50px;")

    # 왼쪽 컨테이너
    container_left = jp.Div(a=container, classes="flex flex-col justify-start", style="width: 55%;")
    
    # 날짜 네비게이션
    nav_container = jp.Div(a=container_left, classes="flex justify-center items-center mb-4", style="gap: 10px;")
    left_button = jp.Button(a=nav_container, text="◀", classes="border rounded px-2 py-1", style="margin-right: 5px; color: #5C5F64; font-size: 12px; padding: 5px 10px; width: 50px; height: 30px;")
    date_range = jp.Div(a=nav_container, text="", classes="text-lg font-bold", style="color: #5C5F64;")
    right_button = jp.Button(a=nav_container, text="▶", classes="border rounded px-2 py-1", style="margin-left: 5px; color: #5C5F64; font-size: 12px; padding: 5px 10px; width: 50px; height: 30px;")

    # 색상 설명 테이블 추가
    color_table = jp.Table(a=container_left, classes="q-table", style="margin-bottom: 20px; border-collapse: collapse; width: 100%;")
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

    # 날짜별 테이블들을 감싸는 컨테이너
    table = jp.Table(a=container_left, style="width:100%")
    
    dates_to_show = dates[:7]
    update_table(dates_to_show, table, selected_times)
    update_date_range(dates_to_show, date_range)

    left_button.on('click', move_left)
    left_button.table = table
    left_button.time_slots = selected_times
    left_button.date_range = date_range

    right_button.on('click', move_right)
    right_button.table = table
    right_button.time_slots = selected_times
    right_button.date_range = date_range

    # 오른쪽 컨테이너
    container_right = jp.Div(a=container, classes="flex flex-col justify-start", style="width: 40%;")
    jp.Div(a=container_right, text="모두가 가능한 시간", style="color: #5C5F64; font-size: 24px; font-weight: bold; margin-bottom: 20px;")

    all_users = list(set().union(*[set(users) for users in selected_times.values()]))
    common_times = get_common_available_times(selected_times, all_users)
    update_common_available_times(container_right, common_times)

    # 버튼들을 감싸는 컨테이너
    button_container = jp.Div(a=container, classes="flex flex-row justify-start", style="gap: 10px;")

    # 시간 등록하기 버튼
    register_button = jp.Button(a=button_container, text="시간 등록하기", classes="border rounded px-2 py-1 bg-blue-500 text-white", style="font-size: 12px; padding: 5px 10px; width: 100px; height: 30px;")
    register_button.select_table = jp.Table(a=container_right, style="width:100%; border: none; margin-bottom: 20px;")
    register_button.dates = dates
    register_button.date_index = date_index
    register_button.on('click', show_select_table)

    # 적용하기 버튼
    apply_button = jp.Button(a=button_container, text="적용하기", classes="border rounded px-2 py-1 bg-green-500 text-white", style="font-size: 12px; padding: 5px 10px; width: 100px; height: 30px;")
    apply_button.select_table = register_button.select_table
    apply_button.table = table
    apply_button.container_right = container_right
    apply_button.on('click', apply_selected_times)

    return wp
