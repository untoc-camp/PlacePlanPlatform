import justpy as jp
import datetime
import calendar

from element.color import MainColors
from element.font import Font

class CalendarComponent:
    def __init__(self):
        self.today = datetime.datetime.today()
        self.select_month = self.today.month
        self.select_year = self.today.year
        self.select_dates = []
        self.calendar = self._getCalendar(self.today.year, self.today.month)
        self.month_name = calendar.month_name[self.today.month]
        self.color = MainColors()
        self.font = Font()
        self.div = None
        self.calendar_div = None  # 달력이 표시될 div를 저장하기 위한 변수
        
        self.default_class = 'p-2 w-10 h-10 text-center items-center justify-center text-white'
        self.rectangle_style = f'position: relative; background-color: {self.color.LightBlueColor}; width: 40px; height: 40px;'
        self.left_cricle_style = f'position: relative;  background-color: {self.color.LightBlueColor}; width: 40px; height: 20px; border-top-left-radius: 20px; border-bottom-left-radius: 20px;'
        self.right_cricle_style = f'position: relative; background-color: {self.color.LightBlueColor}; width: 40px; height: 20px; border-top-right-radius: 20px; border-bottom-right-radius: 20px;'
        self.background_circle_style = f'position: relative; background-color: {self.color.LightBlueColor}; width: 40px; height: 40px; border-top-left-radius: 20px; border-bottom-left-radius: 20px; border-top-right-radius: 20px; border-bottom-right-radius: 20px;'
    
    def _getCalendar(self, year, month):
        calendar_list = []
        cal = calendar.monthcalendar(year, month)
        
        for week in cal:
            week_list = []
            for day in week:
                if day == 0:
                    week_list.append('0')
                else:
                    week_list.append(str(self.select_year) + str(self.select_month).zfill(2) + str(day))
            calendar_list.append(week_list)
        
        return calendar_list
    
    def appendDate(self, msg, *args, **kwargs):
        clicked_date = str(self.select_year) + str(self.select_month).zfill(2) + msg.target.text
        
        parent_row = msg.target.parent_row  # 현재 클릭한 td의 부모 tr 요소
        current_index = parent_row.components.index(msg.target)  # 현재 클릭한 td의 인덱스
        
        left_clicked_date = str(self.select_year) + str(self.select_month).zfill(2) + str(int(msg.target.text) - 1)
        right_clicked_date = str(self.select_year) + str(self.select_month).zfill(2) + str(int(msg.target.text) + 1)
        if clicked_date not in self.select_dates:
            self.select_dates.append(clicked_date)
            
            
            if right_clicked_date in self.select_dates and left_clicked_date in self.select_dates and current_index > 0 and current_index < 6:
                msg.target.set_class = self.default_class
                msg.target.style = self.rectangle_style
                
                left_sibling = parent_row.components[current_index - 1]
                if left_sibling.style == self.background_circle_style:
                    left_sibling.style =  self.left_cricle_style
                else :
                    left_sibling.style = self.rectangle_style
                    for components in left_sibling.components:
                        left_sibling.remove_component(components)

                right_sibling = parent_row.components[current_index + 1]
                if right_sibling.style == self.background_circle_style:
                    right_sibling.style = self.right_cricle_style
                else :
                    right_sibling.style = self.rectangle_style
                    for components in right_sibling.components:
                        right_sibling.remove_component(components)
                
                # 다음 날짜 처리
            elif left_clicked_date in self.select_dates and current_index > 0:
                msg.target.set_class = self.default_class
                msg.target.style = self.right_cricle_style
                left_sibling = parent_row.components[current_index - 1]
                if left_sibling.style == self.background_circle_style:
                    left_sibling.style =  self.left_cricle_style
                else :
                    left_sibling.style = self.rectangle_style
                    for components in left_sibling.components:
                        left_sibling.remove_component(components)

                msg.target.add(jp.Div(text=msg.target.text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))

            elif right_clicked_date in self.select_dates and current_index < 6:
                msg.target.set_class = self.default_class
                msg.target.style = self.left_cricle_style
                right_sibling = parent_row.components[current_index + 1]
                if right_sibling.style == self.background_circle_style:
                    right_sibling.style =  self.right_cricle_style
                else :
                    right_sibling.style = self.rectangle_style
                    for components in right_sibling.components:
                        right_sibling.remove_component(components)
                msg.target.add(jp.Div(text=msg.target.text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))

            else:
                msg.target.set_class = self.default_class
                msg.target.style = self.background_circle_style  

                msg.target.add(jp.Div(text=msg.target.text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))

        else:
            left_sibling_text = str(int(msg.target.text) - 1)
            right_sibling_text = str(int(msg.target.text) + 1)
            self.select_dates.remove(clicked_date)
            msg.target.classes = 'w-10 h-10 text-center items-center p-2 bg-white'
            msg.target.style = ""
            # print("msg에 대한 값입니다", msg.target.components)
            
            msg.target.components = []
            
            if left_clicked_date in self.select_dates and right_clicked_date in self.select_dates and current_index > 0 and current_index < 6:
                left_sibling = parent_row.components[current_index - 1]
                # print("left_sibiling 값", left_sibling)
                if left_sibling.style == self.left_cricle_style:
                    left_sibling.style = self.background_circle_style
                else:
                    left_sibling.style = self.right_cricle_style
                left_sibling.add(jp.Div(text=left_sibling_text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))

                right_sibling = parent_row.components[current_index + 1]
                if right_sibling.style == self.right_cricle_style:
                    right_sibling.style = self.background_circle_style
                else:
                    right_sibling.style = self.left_cricle_style
                right_sibling.add(jp.Div(text=right_sibling_text , classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))                
            
            elif left_clicked_date in self.select_dates and current_index > 0:
                left_sibling = parent_row.components[current_index - 1]
                if left_sibling.style == self.left_cricle_style:
                    left_sibling.style = self.background_circle_style
                else:
                    left_sibling.style = self.right_cricle_style
                left_sibling.add(jp.Div(text=left_sibling_text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))


            elif right_clicked_date in self.select_dates and current_index < 6:
                right_sibling = parent_row.components[current_index + 1]
                if right_sibling.style == self.right_cricle_style:
                    right_sibling.style = self.background_circle_style
                else:
                    right_sibling.style = self.left_cricle_style
                right_sibling.add(jp.Div(text=right_sibling_text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))
            


        # print(self.select_dates)

    def prevMonth(self, msg):
        self.select_month -= 1
        if self.select_month == 0:
            self.select_month = 12
            self.select_year -= 1
        self.updateCalendar()  # 업데이트된 달력을 표시

    # 다음 달로 이동하는 함수
    def nextMonth(self, msg):
        self.select_month += 1
        if self.select_month == 13:
            self.select_month = 1
            self.select_year += 1
        self.updateCalendar()  # 업데이트된 달력을 표시
        
    def showCalendar(self, wp):

        self.wp = wp
        if self.div:
            self.div.delete()  # 이전 달력이 있으면 삭제
        self.div = jp.Div(classes = '')  # 새로운 div 생성
        div = self.div
        div_calendar = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg', style='width: 320px;')
        div_text = jp.Div(text=f'{self.select_year}년 {self.select_month}월', classes = self.font.Heading4_Bold)
        clicked_date = jp.Div(text='', classes='text-lg font-semibold text-blue-500')
        table = jp.Table(classes='table-fixed border-collapse border border-gray-300')
        thead = jp.Thead()
        tbody = jp.Tbody()

        # Create header row with day names
        header_row = jp.Tr()
        for day in calendar.weekheader(2).split():
            header_row.add(jp.Th(text=day, classes='p-2 border border-gray-300'))

        thead.add(header_row)
        cal = self._getCalendar(self.select_year, self.select_month)

        for week in cal:
            row = jp.Tr()
            for day in week:
                if day == '0':
                    row.add(jp.Td(text='', classes='p-2'))
                else:
                    date_str = str(day)[6:]
                    date = jp.Td(text=date_str, classes='w-10 h-10 text-center items-center p-2 bg-white' + self.font.Body1_Regular)  # 초기 배경색을 흰색으로 설정
                    date.parent_row = row
                    date.on('click', self.appendDate)
                    row.add(date)
            tbody.add(row)

        table.add(thead, tbody)

        # 이전 달과 다음 달로 이동하는 화살표
        left_arrow = jp.Div(text='<', classes='cursor-pointer inline-block' + self.font.Heading2_Bold)
        right_arrow = jp.Div(text='>', classes='cursor-pointer inline-block' + self.font.Heading2_Bold)
        left_arrow.on('click', self.prevMonth)
        right_arrow.on('click', self.nextMonth)

        # 달력과 화살표를 div_calendar에 추가
        div_calendar.add(jp.Div(classes='flex items-center justify-between', children=[left_arrow, div_text, right_arrow]))
        div_calendar.add(table)
        div_calendar.add(clicked_date)
        div.add(div_calendar)
        wp.add(self.div)
        
    def updateCalendar(self):
        if self.div:
            # div가 이미 존재하면, 기존 내용을 업데이트
            self.div.delete_components()  # div 내의 모든 컴포넌트 삭제
            
            # 새로운 달력 내용으로 div 업데이트
            div_calendar = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg', style='width: 320px;')
            div_text = jp.Div(text=f'{self.select_year}년 {self.select_month}월', classes = self.font.Heading4_Bold)
            clicked_date = jp.Div(text='', classes='text-lg font-semibold text-blue-500')
            table = jp.Table(classes='table-fixed border-collapse border border-gray-300')
            thead = jp.Thead()
            tbody = jp.Tbody()

            # 헤더 행 생성
            header_row = jp.Tr()
            for day in calendar.weekheader(2).split():
                header_row.add(jp.Th(text=day, classes='p-2 border border-gray-300'))
            thead.add(header_row)
            
            # 달력 데이터 생성
            cal = self._getCalendar(self.select_year, self.select_month)
            for week in cal:
                row = jp.Tr()
                for day in week:
                    if day == '0':
                        row.add(jp.Td(text='', classes='p-2'))
                    else:
                        date_str = str(day)[6:]
                        date = jp.Td(text=date_str, classes='w-10 h-10 text-center items-center p-2 bg-white' + self.font.Body1_Regular)
                        date.parent_row = row
                        date.on('click', self.appendDate)
                        row.add(date)
                tbody.add(row)

            table.add(thead, tbody)

            # 이전 및 다음 달로 이동하는 화살표 추가
            left_arrow = jp.Div(text='<', classes='cursor-pointer inline-block' + self.font.Heading2_Bold)
            right_arrow = jp.Div(text='>', classes='cursor-pointer inline-block' + self.font.Heading2_Bold)
            left_arrow.on('click', self.prevMonth)
            right_arrow.on('click', self.nextMonth)
            
            div_calendar.add(jp.Div(classes='flex items-center justify-between', children=[left_arrow, div_text, right_arrow]))

            div_calendar.add(table)
            div_calendar.add(clicked_date)
            self.div.add(div_calendar)
        else:
            # div가 존재하지 않으면, 처음부터 달력을 생성
            self.showCalendar(self.wp)

            