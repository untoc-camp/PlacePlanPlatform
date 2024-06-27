import justpy as jp

from element.color import MainColors
from element.font import Font
from element.header import Header

def TimePromiseMainView():
    wp = jp.WebPage()
    head = Header("/timepromise/make")
    head.show_header(wp)
    
    # 상단 섹션
    top_section = jp.Div(classes="flex justify-between items-center p-4 border-b", a=wp)
    jp.P(text='가능한 시간', classes='text-xl font-semibold', a=top_section)
    jp.Button(text='약속 만들기', classes='bg-blue-100 hover:bg-blue-200 text-blue-800 py-2 px-4 rounded-full flex items-center', a=top_section, style="margin-right: 10px;")
    
    appointment_app = AppointmentApp()
    appointment_app.add_appointment_page(wp=wp)
    
    return wp

class AppointmentApp:
    def __init__(self):
        self.appointments = []  # 약속 목록 저장 리스트
        self.font = Font()
        self.color = MainColors()
        self.grid = None
        self.add_button_div = None

    def add_appointment_page(self, wp):
        # 약속 목록을 담을 그리드
        self.grid = jp.Div(classes="grid grid-cols-2 md:grid-cols-3 gap-4 p-4", style="display: grid; grid-auto-flow: dense;", a=wp)

        # 추가하기 버튼
        self.add_button_div = jp.Div(classes="border rounded-lg shadow-md p-4 flex justify-center items-center cursor-pointer hover:bg-gray-100", style="height: 180px; width: 100%; order: 9999;", a=self.grid)
        jp.Icon(icon='add', classes='text-3xl text-gray-500', a=self.add_button_div)
        jp.P(text='추가하기', classes='text-sm text-gray-500 mt-2', a=self.add_button_div)
        
        # 추가하기 버튼 클릭 이벤트
        self.add_button_div.on('click', self.add_new_appointment_click)

        return wp

    def add_new_appointment_click(self, msg):
        self.add_new_appointment()

    def add_new_appointment(self):
        # 약속 담길 div 생성
        appointment_div = jp.Div(classes="border rounded-lg shadow-md p-4", style="border-color: #e5e7eb; background-color: #ffffff; height: 180px;")
        self.appointments.append(appointment_div)  # 약속 목록에 추가

        # 약속 정보 추가
        jp.P(text='약속명이 들어갈 공간입니다', classes="text-base font-medium text-gray-900 mb-2", a=appointment_div)  # 약속명
        jp.Div(text='24.01.01 ~ 24.01.13', classes='text-sm text-gray-500 mb-1', a=appointment_div)  # 날짜
        jp.Div(text='4명', classes='text-sm text-gray-500 mb-1', a=appointment_div)  # 참여 인원
        jp.Div(text='미정', classes='text-sm text-gray-500 mb-2', a=appointment_div)  # 위치
        jp.Button(text='공유하기', classes='bg-blue-100 hover:bg-blue-200 text-blue-800 text-sm py-1 px-3 rounded-full', a=appointment_div, style="margin-top: 10px;")

        # 그리드에 약속 추가
        self.grid.add(appointment_div)

