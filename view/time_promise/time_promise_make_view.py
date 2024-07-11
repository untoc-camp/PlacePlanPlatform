import justpy as jp
import os
import json
from element.color import MainColors
from element.font import Font
from element.calendar import CalendarComponent
from element.header import Header

class AppointmentPage:
    def __init__(self):
        self.color = MainColors()
        self.font = Font()
        self.calendar = CalendarComponent()
        self.appointment_place_select = None  # 약속 장소 선택란을 저장할 변수
        self.appointment_type_select = None  # 약속 종류 선택란을 저장할 변수
        self.calendar_div = jp.Div(classes='w-1/3 bg-white-100 p-4 rounded-md')
        self.place_input = None
        self.type_input = None

    def toggle_color(self, msg):
        if 'bg-blue-500' in msg.target.classes:
            msg.target.classes = 'w-8 h-48 border-2 border-gray-400 bg-white rounded'
        else:
            msg.target.classes = 'w-8 h-48 border-2 border-gray-400 bg-blue-500 rounded'

    def time_dropdown_select(self, msg):
        if msg.target.value == 'weekday':
            self.calendar.resetCalendar()
            self.calendar_div.delete_components()

            title = jp.P(text='시간을 정해주세요', classes='text-xl font-bold mb-2 text-center')
            description = jp.P(text='요일을 선택할 수 있습니다.', classes='text-gray-600 mb-2 text-center')
            description2 = jp.P(text='특정 일을 선택할 수도 있습니다.', classes='text-gray-600 mb-4 text-center')

            selection_dropdown = jp.Select(classes='block w-2/3 mx-auto mb-4', style='width: 200px;')
            selection_dropdown.add(jp.Option(text='특정 일 선택', value='day'))  # 특정 일 선택 옵션 선택 상태 해제
            selection_dropdown.add(jp.Option(text='요일 선택', value=''))  # 요일 선택 옵션 선택 상태 설정
            selection_dropdown.on('change', self.time_dropdown_select)
            self.calendar_div.add(title, description, description2, selection_dropdown)
            days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

            # 전체 컨테이너 설정
            container = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg', style='width: 320px;', a=self.calendar_div)

            # 막대들을 담을 내부 컨테이너
            inner_container = jp.Div(classes='flex flex-col items-center', a=container)

            # 요일별 막대 컨테이너
            bars_container = jp.Div(classes='flex', a=inner_container)

            # 각 요일 막대 추가
            for day in days:
                day_container = jp.Div(classes='flex flex-col items-center mx-1', a=bars_container)
                jp.Div(text=day, classes='mb-2', a=day_container)
                bar = jp.Div(classes='w-8 h-48 border-2 border-gray-400 bg-white rounded', a=day_container)
                bar.on('click', self.toggle_color)  # 막대를 클릭하면 색상 바뀜

        else:
            self.calendar.resetCalendar()
            self.calendar_div.delete_components()

            title = jp.P(text='시간을 정해주세요', classes='text-xl font-bold mb-2 text-center')
            description = jp.P(text='요일을 선택할 수 있습니다.', classes='text-gray-600 mb-2 text-center')
            description2 = jp.P(text='특정 일을 선택할 수도 있습니다.', classes='text-gray-600 mb-2 text-center')
            selection_dropdown = jp.Select(classes='block w-2/3 mx-auto mb-4', style='width: 200px;')
            selection_dropdown.add(jp.Option(text='특정 일 선택', value=''))  # 특정 일 선택 옵션 선택 상태 설정
            selection_dropdown.add(jp.Option(text='요일 선택', value='weekday'))  # 요일 선택 옵션 선택 상태 해제
            selection_dropdown.on('change', self.time_dropdown_select)
            self.calendar_div.add(title, description, description2, selection_dropdown)
            self.calendar.showCalendar(self.calendar_div)

    def appointment_page(self):
        wp = jp.WebPage()
        head = Header("/timepromise/make")
        head.show_header(wp)

        # 이벤트 이름 입력 필드
        event_name_container = jp.Div(classes='flex justify-center mt-10')
        self.event_name_input = jp.Input(placeholder='New Event Name',
                                         classes='block w-1/3 p-2 text-center border rounded',
                                         style='border-width: 2px; border-color: black;')
        event_name_container.add(self.event_name_input)

        # 이전 페이지로 이동하는 화살표
        back_arrow = jp.A(text='<', href='/timepromise', classes='cursor-pointer absolute top-20 left-5 ' + self.font.Heading2_Bold)

        # 달력과 약속 정보를 담을 컨테이너
        main_container = jp.Div(classes='flex justify-between mt-10', style='width: 80%; margin: 0 auto;')

        # 달력을 담을 div
        title = jp.P(text='시간을 정해주세요', classes='text-xl font-bold mb-2 text-center')
        description = jp.P(text='요일을 선택할 수 있습니다.', classes='text-gray-600 mb-2 text-center')
        description2 = jp.P(text='특정 일을 선택할 수도 있습니다.', classes='text-gray-600 mb-4 text-center')

        selection_dropdown = jp.Select(classes='block w-2/3 mx-auto mb-4', style='width: 200px;')
        selection_dropdown.add(jp.Option(text='특정 일 선택', value='', classes='text-gray-500'))  # 선택 가능하도록 변경
        selection_dropdown.add(jp.Option(text='요일 선택', value='weekday'))  # 선택 상태 해제
        selection_dropdown.on('change', self.time_dropdown_select)
        self.calendar_div.add(title, description, description2, selection_dropdown)
        self.calendar.showCalendar(self.calendar_div)
        
        # 약속 정보를 담을 컨테이너
        right_container = jp.Div(classes='flex flex-col w-1/3 h-96 justify-between')
        # 약속 멘트 정보를 담을 div
        appointment_ment_div = jp.Div(classes='w-full bg-white-100 p-4 rounded-md', style='margin-bottom: 0;')

        title = jp.P(text='몇시에 만날래?', classes='text-xl font-bold mb-2 text-center')
        description = jp.P(text='시작시간 및 끝나는 시간을 선택해 주세요.', classes='text-gray-600 mb-2 text-center')
        description2 = jp.P(text='약속 장소를 선택해 주세요.', classes='text-gray-600 mb-4 text-center')

        appointment_ment_div.add(title, description, description2)

        # 약속 정보를 담을 div
        appointment_info_div = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg mt-1', style='width: 400px; height: 320px;')

        # 시작 시간 선택
        start_time_container = jp.Div(classes='flex items-center mb-4')
        start_time_container.add(jp.P(text='시작 시간:', classes='mr-2'))

        self.start_hour_select = jp.Select(classes='block w-1/3')
        self.start_hour_select.add(jp.Option(text='09시', value='', disabled=True, selected=True, classes='text-gray-500'))
        for hour in range(9, 24):
            self.start_hour_select.add(jp.Option(text=str(hour).zfill(2), value=str(hour).zfill(2)))
        start_time_container.add(self.start_hour_select)

        self.start_minute_select = jp.Select(classes='block w-1/3 ml-2')
        self.start_minute_select.add(jp.Option(text='00분', value='', disabled=True, selected=True, classes='text-gray-500'))
        for minute in range(0, 60, 5):
            self.start_minute_select.add(jp.Option(text=str(minute).zfill(2), value=str(minute).zfill(2)))
        start_time_container.add(self.start_minute_select)

        # 끝나는 시간 선택
        end_time_container = jp.Div(classes='flex items-center mb-4')
        end_time_container.add(jp.P(text='끝나는 시간:', classes='mr-2'))

        self.end_hour_select = jp.Select(classes='block w-1/3')
        self.end_hour_select.add(jp.Option(text='18시', value='', disabled=True, selected=True, classes='text-gray-500'))
        for hour in range(9, 25):
            self.end_hour_select.add(jp.Option(text=str(hour).zfill(2), value=str(hour).zfill(2)))
        end_time_container.add(self.end_hour_select)

        self.end_minute_select = jp.Select(classes='block w-1/3 ml-2')
        self.end_minute_select.add(jp.Option(text='00분', value='', disabled=True, selected=True, classes='text-gray-500'))
        for minute in range(0, 60, 5):
            self.end_minute_select.add(jp.Option(text=str(minute).zfill(2), value=str(minute).zfill(2)))
        end_time_container.add(self.end_minute_select)

        appointment_info_div.add(start_time_container)
        appointment_info_div.add(end_time_container)

        # 지역 선택
        appointment_info_div.add(jp.P(text='지역 선택:', classes='mt-4'))
        self.appointment_place_select = jp.Select(classes='block w-full mt-2 mb-4')
        self.appointment_place_select.add(jp.Option(text='장소 선택하세요', value='', disabled=True, selected=True, classes='text-gray-500'))
        self.appointment_place_select.add(jp.Option(text='부산대', value='부산대'))
        self.appointment_place_select.add(jp.Option(text='서면', value='서면'))
        self.appointment_place_select.add(jp.Option(text='광안리', value='광안리'))
        self.appointment_place_select.add(jp.Option(text='남포', value='남포'))
        self.appointment_place_select.add(jp.Option(text='기타', value='기타'))

        # 지역 선택 후
        self.place_input = jp.Input(type='text', classes='block w-full mt-2 mb-4', placeholder='추가 장소 정보를 입력하세요')
        
        appointment_info_div.add(self.appointment_place_select)
        appointment_info_div.add(self.place_input)

        # 약속 종류 선택
        appointment_info_div.add(jp.P(text='약속 종류:', classes='mt-4'))
        self.appointment_type_select = jp.Select(classes='block w-full mt-2 mb-4')
        self.appointment_type_select.add(jp.Option(text='종류를 선택하세요', value='', disabled=True, selected=True, classes='text-gray-500'))
        self.appointment_type_select.add(jp.Option(text='밥약속', value='밥약속'))
        self.appointment_type_select.add(jp.Option(text='술약속', value='술약속'))
        self.appointment_type_select.add(jp.Option(text='회의', value='회의'))
        self.appointment_type_select.add(jp.Option(text='기타', value='기타'))

        appointment_info_div.add(self.appointment_type_select)

        # 약속 종류 선택 후
        self.type_input = jp.Input(type='text', classes='block w-full mt-2 mb-4', placeholder='추가 약속 정보를 입력하세요')

        appointment_info_div.add(self.type_input)


        # 약속 추가 버튼
        add_appointment_button = jp.Button(text='약속 추가', classes='bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded mt-4')
        add_appointment_button.on('click', self.save_appointment)
        appointment_info_div.add(add_appointment_button)

        # right_container에 약속 멘트 div와 약속 정보 div 추가
        right_container.add(appointment_ment_div, appointment_info_div)

        main_container.add(self.calendar_div, right_container)
        wp.add(event_name_container, back_arrow, main_container)
        return wp

    # 약속 정보를 저장하는 함수
    def save_appointment(self, msg):
        event_name = self.event_name_input.value
        start_hour = self.start_hour_select.value
        start_minute = self.start_minute_select.value
        end_hour = self.end_hour_select.value
        end_minute = self.end_minute_select.value
        place = self.appointment_place_select.value
        place_detail = self.place_input.value
        appointment_type = self.appointment_type_select.value
        type_detail = self.type_input.value

        # 필수 필드 확인
        if not all([event_name, start_hour, start_minute, end_hour, end_minute, place, appointment_type]):
            jp.run_task(self.show_warning_message(msg, "모든 필수 항목을 입력해주세요."))
            return

        # 약속 정보를 JSON 형식으로 저장
        appointment_data = {
            'event_name': event_name,
            'start_time': f"{start_hour}:{start_minute}",
            'end_time': f"{end_hour}:{end_minute}",
            'place': place,
            'place_detail': place_detail,
            'appointment_type': appointment_type,
            'type_detail': type_detail
        }

       

        # JSON 파일에 저장
        file_path = 'data/appointments.json'
        try:
            data = []
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                except UnicodeDecodeError:
                    # UTF-8로 읽기 실패시 cp949로 시도
                    with open(file_path, 'r', encoding='cp949') as file:
                        data = json.load(file)

            data.append(appointment_data)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            jp.run_task(self.show_success_message(msg))
        except Exception as e:
            error_message = f"약속 저장 중 오류 발생: {str(e)}"
            print(error_message)  # 콘솔에 오류 출력
            jp.run_task(self.show_warning_message(msg, error_message))
            

    async def show_success_message(self, msg):
        success_message = jp.Div(
            text='약속이 성공적으로 추가되었습니다!',
            classes='bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative',
            a=msg.page
        )
        await jp.run_task(self.remove_message(success_message))
    async def show_warning_message(self, msg, warning_text):
        warning_message = jp.Div(
            text=warning_text,
            classes='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative',
            a=msg.page
        )
        await jp.run_task(self.remove_message(warning_message))


    async def remove_message(self, message):
        await jp.sleep(3)
        message.delete()


def TimePromiseMakeView():
    appointment_page = AppointmentPage()
    return appointment_page.appointment_page()
