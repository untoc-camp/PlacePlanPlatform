import justpy as jp
from element.color import MainColors
from element.font import Font
from element.calendar import CalendarComponent

class AppointmentPage:
    def __init__(self):
        self.color = MainColors()
        self.font = Font()
        self.calendar = CalendarComponent()
        self.custom_type_input = None  # 직접 작성 입력란을 저장할 변수
        
    def appointment_page(self):
        wp = jp.WebPage()
        
        # 이전 페이지로 이동하는 화살표
        back_arrow = jp.Div(text='<', classes='cursor-pointer absolute top-5 left-5 ' + self.font.Heading2_Bold)
        back_arrow.on('click', self.go_back)
        
        # 달력과 약속 정보를 담을 컨테이너
        main_container = jp.Div(classes='flex justify-center mt-10')
        
        # 달력을 담을 div
        calendar_div = jp.Div(classes='w-2/5 h-96 bg-white-100 p-4 rounded-md mr-5')
        self.calendar.showCalendar(calendar_div)
        
        # 약속 정보를 넣을 div
        appointment_info_div = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg', style='width: 360px; height: 360px;')
        
        # 시작 시간 선택
        start_time_container = jp.Div(classes='flex items-center mb-4')
        start_time_container.add(jp.P(text='시작 시간:', classes='mr-2'))
        
        start_hour_select = jp.Select(classes='block w-1/3')
        start_hour_select.add(jp.Option(text='09시', value='', disabled=True, selected=True, classes='text-gray-500'))
        for hour in range(9, 24):
            start_hour_select.add(jp.Option(text=str(hour).zfill(2), value=str(hour).zfill(2)))
        start_time_container.add(start_hour_select)
        
        start_minute_select = jp.Select(classes='block w-1/3 ml-2')
        start_minute_select.add(jp.Option(text='00분', value='', disabled=True, selected=True, classes='text-gray-500'))
        for minute in range(0, 60, 5):
            start_minute_select.add(jp.Option(text=str(minute).zfill(2), value=str(minute).zfill(2)))
        start_time_container.add(start_minute_select)
        
        # 끝나는 시간 선택
        end_time_container = jp.Div(classes='flex items-center mb-4')
        end_time_container.add(jp.P(text='끝나는 시간:', classes='mr-2'))
        
        end_hour_select = jp.Select(classes='block w-1/3')
        end_hour_select.add(jp.Option(text='18시', value='', disabled=True, selected=True, classes='text-gray-500'))
        for hour in range(9, 25):
            end_hour_select.add(jp.Option(text=str(hour).zfill(2), value=str(hour).zfill(2)))
        end_time_container.add(end_hour_select)
        
        end_minute_select = jp.Select(classes='block w-1/3 ml-2')
        end_minute_select.add(jp.Option(text='00분', value='', disabled=True, selected=True, classes='text-gray-500'))
        for minute in range(0, 60, 5):
            end_minute_select.add(jp.Option(text=str(minute).zfill(2), value=str(minute).zfill(2)))
        end_time_container.add(end_minute_select)
        
        appointment_info_div.add(start_time_container)
        appointment_info_div.add(end_time_container)
        
        # 지역 선택
        appointment_info_div.add(jp.P(text='지역 선택:', classes='mt-4'))
        self.appointment_place_select = jp.Select(classes='block w-full mt-2')
        self.appointment_place_select.add(jp.Option(text='장소 선택하세요', value='', disabled=True, selected=True, classes='text-gray-500'))
        self.appointment_place_select.add(jp.Option(text='부산대', value='부산대'))
        self.appointment_place_select.add(jp.Option(text='서면', value='서면'))
        self.appointment_place_select.add(jp.Option(text='광안리', value='광안리'))
        self.appointment_place_select.add(jp.Option(text='남포', value='남포'))        
        self.appointment_place_select.add(jp.Option(text='직접 작성', value='직접 작성'))
        appointment_info_div.add(self.appointment_place_select)
        # 약속 종류 선택
        appointment_info_div.add(jp.P(text='약속 종류:', classes='mt-4'))
        self.appointment_type_select = jp.Select(classes='block w-full mt-2')
        self.appointment_type_select.add(jp.Option(text='종류를 선택하세요', value='', disabled=True, selected=True, classes='text-gray-500'))
        self.appointment_type_select.add(jp.Option(text='미정', value='종류는 미정'))
        self.appointment_type_select.add(jp.Option(text='밥약속', value='밥약속'))
        self.appointment_type_select.add(jp.Option(text='술약속', value='술약속'))
        self.appointment_type_select.add(jp.Option(text='회의', value='회의'))
        self.appointment_type_select.add(jp.Option(text='직접 작성', value='직접 작성'))
        self.appointment_type_select.on('change', self.show_custom_type_input)
        appointment_info_div.add(self.appointment_type_select)
        
        # 약속 추가 버튼
        appointment_info_div.add(jp.Button(text='약속 추가', classes='bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded mt-4'))

        main_container.add(calendar_div, appointment_info_div)
        wp.add(back_arrow, main_container)
        return wp
    
    # 약속 종류 선택 시 직접 작성 입력란을 보여줌
    def show_custom_type_input(self, msg):
        if msg.value == '직접 작성':
            self.custom_type_input = jp.Input(type='text', classes='block w-full mt-2', placeholder='약속 종류를 입력하세요')
            self.appointment_type_select.after(self.custom_type_input)
        else:
            if self.custom_type_input:
                self.custom_type_input.delete()

    # 뒤로가기
    def go_back(self, msg):
        msg.page.redirect('/timepromise')


def TimePromiseMakeView():
    appointment_page = AppointmentPage()
    return appointment_page.appointment_page()