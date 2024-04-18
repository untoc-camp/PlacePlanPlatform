import justpy as jp
import datetime
import calendar

class CalendarComponent:
    def __init__(self):
        self.today = datetime.datetime.today()
        self.select_month = self.today.month
        self.select_year = self.today.year
        self.select_dates = []
        self.calendar = self._get_calendar(self.today.year, self.today.month)
        self.month_name = calendar.month_name[self.today.month]
        
    def _get_calendar(self, year, month):
        calendar_list = []
        cal = calendar.monthcalendar(year, month)
        
        for week in cal:
            week_list = []
            for day in week:
                if day == 0:
                    week_list.append(0)
                else:
                    week_list.append(str(self.select_year) + str(self.select_month).zfill(2) + str(day))
            calendar_list.append(week_list)
        
        return calendar_list
    
    def show_calendar(self, wp):
        div = jp.Div(classes='flex items-center justify-center h-screen')
        div_calendar = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg')
        div_text = jp.Div(text=f'{self.select_year} {self.select_month}', classes='text-xl font-bold mb-4')
        clicked_date = jp.Div(text='', classes='text-lg font-semibold text-blue-500')

        table = jp.Table(classes='table-fixed w-full border-collapse border border-gray-300')
        thead = jp.Thead()
        tbody = jp.Tbody()

        # Create header row with day names
        header_row = jp.Tr()
        for day in calendar.weekheader(1).split():
            header_row.add(jp.Th(text = day, classes='p-2 border border-gray-300'))

        thead.add(header_row)
        cal = self._get_calendar(self.select_year, self.select_month)

        for week in cal:
            row = jp.Tr()
            for day in week:
                if day == 0:
                    row.add(jp.Td(text='', classes='p-2 border border-gray-300'))
                else:
                    date = jp.Td(text=str(day), classes='p-2 ')

                    row.add(date)
            tbody.add(row)

        table.add(thead, tbody)
        div_calendar.add(div_text, table, clicked_date)
        div.add(div_calendar)
        wp.add(div)