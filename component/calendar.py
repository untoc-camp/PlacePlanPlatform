import justpy as jp
import datetime
import calendar

from component.color import MainColors

class CalendarComponent:
    def __init__(self):
        self.today = datetime.datetime.today()
        self.select_month = self.today.month
        self.select_year = self.today.year
        self.select_dates = []
        self.calendar = self._get_calendar(self.today.year, self.today.month)
        self.month_name = calendar.month_name[self.today.month]
        self.color = MainColors()

        self.default_class = 'p-2 w-10 h-10 text-center items-center justify-center text-white'
        self.rectangle_style = f'position: relative; background-color: {self.color.LightBlueColor}; width: 40px; height: 40px;'
        self.left_cricle_style = f'position: relative; border-radius: 9999px; background-color: {self.color.LightBlueColor}; width: 40px; height: 20px; border-top-right-radius: 20px; border-bottom-right-radius: 20px;'
        self.right_cricle_style = f'position: relative; border-radius: 9999px; background-color: {self.color.LightBlueColor}; width: 40px; height: 20px; border-top-left-radius: 20px; border-bottom-left-radius: 20px;'
        self.background_circle_style = f'position: relative; border-radius: 9999px; background-color: {self.color.LightBlueColor}; width: 40px; height: 40px;'
    def _get_calendar(self, year, month):
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
    
    def append_date(self, msg, *args, **kwargs):
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
                    left_sibling.remove_component(left_sibling.components[0])
                
                
                right_sibling = parent_row.components[current_index + 1]
                if right_sibling.style == self.background_circle_style:
                    right_sibling.style = self.right_cricle_style
                else :
                    right_sibling.style = self.rectangle_style
                    right_sibling.remove_component(right_sibling.components[0])
                
                # 다음 날짜 처리
            elif left_clicked_date in self.select_dates and current_index > 0:
                msg.target.set_class = self.default_class
                msg.target.style = self.right_cricle_style
                left_sibling = parent_row.components[current_index - 1]
                if left_sibling.style == self.background_circle_style:
                    left_sibling.style =  self.left_cricle_style
                else :
                    left_sibling.style = self.rectangle_style
                    left_sibling.remove_component(left_sibling.components[0])

                msg.target.add(jp.Div(text=msg.target.text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))

            elif right_clicked_date in self.select_dates and current_index < 6:
                msg.target.set_class = self.default_class
                msg.target.style = self.left_cricle_style
                right_sibling = parent_row.components[current_index + 1]
                if right_sibling.style == self.background_circle_style:
                    right_sibling.style =  self.right_cricle_style
                else :
                    right_sibling.style = self.rectangle_style
                    right_sibling.remove_component(right_sibling.components[0])
                msg.target.add(jp.Div(text=msg.target.text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))

            else:
                msg.target.set_class = self.default_class
                msg.target.style = self.background_circle_style  # width와 height를 조정하여 원 모양의 크기를 조절
                # 원 모양 추가: 원을 중앙에 배치하고, 텍스트를 위로 오게 하려면, 원을 배경으로 하고 텍스트를 전면에 배치
                msg.target.add(jp.Div(text=msg.target.text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))

        else:
            left_sibling_text = str(int(msg.target.text) - 1)
            right_sibling_text = str(int(msg.target.text) + 1)
            self.select_dates.remove(clicked_date)
            msg.target.classes = 'w-10 h-10 text-center items-center p-2 bg-white'
            msg.target.style = ""
            print(msg)
            if msg.target.components:
                msg.target.remove_component(msg.target.components[0])

            if left_clicked_date in self.select_dates and right_clicked_date in self.select_dates and current_index > 0 and current_index < 6:
                left_sibling = parent_row.components[current_index - 1]
                if left_sibling.style == self.left_cricle_style:
                    print("!!!")
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
                    left_sibling.style = self.rectangle_style
                left_sibling.add(jp.Div(text=left_sibling_text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))


            elif right_clicked_date in self.select_dates and current_index < 6:
                right_sibling = parent_row.components[current_index + 1]
                if right_sibling.style == self.right_cricle_style:
                    right_sibling.style = self.background_circle_style
                else:
                    right_sibling.style = self.rectangle_style
                right_sibling.add(jp.Div(text=right_sibling_text, classes="absolute p-2 w-10 h-10 text-center items-center justify-center text-white", style=f'z-index: 2; background-color: {self.color.MainColor}; border-radius: 9999px; top: 50%; left: 50%; transform: translate(-50%, -50%);'))
            


        print(self.select_dates)



    def show_calendar(self, wp):
        div = jp.Div(classes='')
        div_calendar = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg')
        div_text = jp.Div(text=f'{self.select_year}년 {self.select_month}월', classes='text-xl font-bold mb-4')
        clicked_date = jp.Div(text='', classes='text-lg font-semibold text-blue-500')
        table = jp.Table(classes='table-fixed border-collapse border border-gray-300')
        thead = jp.Thead()
        tbody = jp.Tbody()

        # Create header row with day names
        header_row = jp.Tr()
        for day in calendar.weekheader(2).split():
            header_row.add(jp.Th(text=day, classes='p-2 border border-gray-300'))

        thead.add(header_row)
        cal = self._get_calendar(self.select_year, self.select_month)

        for week in cal:
            row = jp.Tr()
            for day in week:
                if day == '0':
                    row.add(jp.Td(text='', classes='p-2'))
                else:
                    date_str = str(day)[6:]
                    date = jp.Td(text=date_str, classes='w-10 h-10 text-center items-center p-2 bg-white')  # 초기 배경색을 흰색으로 설정
                    date.parent_row = row
                    date.on('click', self.append_date)
                    row.add(date)
            tbody.add(row)

        table.add(thead, tbody)
        div_calendar.add(div_text, table, clicked_date)
        div.add(div_calendar)
        wp.add(div)
