import justpy as jp
import json
from element.color import MainColors
from element.font import Font
from element.header import Header

class AppointmentApp:
    def __init__(self):
        self.appointments = []
        self.font = Font()
        self.color = MainColors()
        self.grid = None

    def load_appointments(self):
        try:
            with open('data/appointments.json', 'r', encoding='utf-8') as file:
                self.appointments = json.load(file)
        except FileNotFoundError:
            print("data/appointments.json 파일을 찾을 수 없습니다.")
            self.appointments = []
        except json.JSONDecodeError:
            print("JSON 파일 형식이 올바르지 않습니다.")
            self.appointments = []

    def save_appointments(self):
        with open('data/appointments.json', 'w', encoding='utf-8') as file:
            json.dump(self.appointments, file, ensure_ascii=False, indent=4)

    def add_appointment_page(self, wp):
        self.load_appointments()
        self.grid = jp.Div(classes="grid grid-cols-2 md:grid-cols-3 gap-4 p-4", style="display: grid; grid-auto-flow: dense;", a=wp)
        for appointment in self.appointments:
            self.add_appointment_to_grid(appointment)
        return wp

    def add_appointment_to_grid(self, appointment):
        appointment_div = jp.Div(classes="border rounded-lg shadow-md p-4", style="border-color: #e5e7eb; background-color: #ffffff; height: 180px;")
        
        # 이벤트 이름 (비어있으면 'Blank'로 표시)
        event_name = appointment.get('event_name') or 'Blank'
        jp.P(text=event_name, classes="text-base font-medium text-gray-900 mb-2", a=appointment_div)
        
        # 약속 시간 (start_time이 비어있으면 '09:00', end_time이 비어있으면 '18:00'으로 설정)
        start_time = '09:00' if appointment.get('start_time') == '' else appointment.get('start_time')
        end_time = '18:00' if appointment.get('end_time') == '' else appointment.get('end_time')
        jp.Div(text=f"약속시간 : {start_time} ~ {end_time}", classes='text-sm text-gray-500 mb-1', a=appointment_div)
        
        # 약속 장소
        place = appointment.get('place', '')
        jp.Div(text=f"약속장소 : {place}", classes='text-sm text-gray-500 mb-1', a=appointment_div)
        
        # 약속 유형 (비어있어도 '약속 유형:' 출력)
        appointment_type = appointment.get('appointment_type', '')
        jp.Div(text=f"약속 유형: {appointment_type}", classes='text-sm text-gray-500 mb-2', a=appointment_div)
        
        # 버튼 컨테이너 추가
        button_container = jp.Div(classes="flex justify-between items-center mt-4", a=appointment_div)
        
        jp.A(text='일정 수정하기', href='/timepromise/make', classes='bg-blue-100 hover:bg-blue-200 text-blue-800 text-sm py-1 px-3 rounded-full', a=button_container)

        delete_button = jp.Button(text="삭제", classes="bg-red-100 hover:bg-red-200 text-red-800 text-sm py-1 px-3 rounded-full", a=button_container)
        delete_button.on('click', self.delete_appointment)
        delete_button.appointment = appointment
        delete_button.appointment_div = appointment_div

        self.grid.add(appointment_div)

    def delete_appointment(self, msg):
            appointment = msg.target.appointment
            appointment_div = msg.target.appointment_div

            if appointment in self.appointments:
                self.appointments.remove(appointment)
                self.save_appointments()
                appointment_div.remove()
                msg.page.update()

def TimePromiseMainView():
    wp = jp.WebPage()
    head = Header("/timepromise/main")
    head.show_header(wp)
    
    # 상단 섹션
    top_section = jp.Div(classes="flex justify-between items-center p-4 border-b", a=wp)
    jp.P(text='가능한 시간', classes='text-xl font-semibold', a=top_section)
    jp.A(text='약속 만들기', href='/timepromise/make', classes='bg-blue-100 hover:bg-blue-200 text-blue-800 py-2 px-4 rounded-full flex items-center', a=top_section, style="margin-right: 10px;")
    
    appointment_app = AppointmentApp()
    appointment_app.add_appointment_page(wp=wp)
    
    return wp

# 파일 끝에 다음 줄 추가
__all__ = ['TimePromiseMainView']