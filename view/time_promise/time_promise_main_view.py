import justpy as jp

from element.color import MainColors
from element.font import Font

def TimePromiseMainView():
    wp = jp.WebPage()
    wp.add(jp.P(text='시간약속페이지', classes='text-5xl m-2'))
    AppointmentApp().add_appointment_page(wp=wp)
    return wp

class AppointmentApp:
    def __init__(self):
        self.appointments = []  # 약속 목록 저장 리스트
        self.font = Font()
        self.color = MainColors()

    def add_appointment_page(self, wp):
        # 약속 추가 버튼
        add_button = jp.Button(text='약속 만들기', classes='bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded m-2' + self.font.Body1_Bold, a=wp)
        
        # 약속 목록을 담을 그리드
        self.grid = jp.Div(classes="grid grid-cols-3 gap-4 m-4", a=wp)

        # 버튼 클릭하면 약속 추가
        add_button.on('click', self.add_new_appointment)

        return wp

    def add_new_appointment(self, msg):
        # 약속 담길 div 생성
        appointment_div = jp.Div(classes = f"border-2 p-2 rounded", style = f"border-color: {self.color.MainColor};")
        appointment_div.style = f"margin: 10px; border-color: {self.color.MainColor};"
        self.appointments.append(appointment_div)  # 약속 목록에 추가

        # 약속 정보 추가
        jp.P(text='약속 명', classes=self.font.Heading4_Bold, a=appointment_div)   # 추후에 변수 연결 예정 ------------------------- 
        jp.Div(text='날짜: #날짜', classes='flex items-center', a=appointment_div)
        jp.Div(text='참여 인원: #n명', classes='flex items-center', a=appointment_div)
        jp.Div(text='위치: #위치명', classes='flex items-center', a=appointment_div)
        jp.Div(text='공유하기', classes='flex items-center justify-end', a=appointment_div)

        # 그리드에 약속 div 추가
        appointment_div.add_to(self.grid)
