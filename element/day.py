import justpy as jp

# 막대를 클릭하면 색상을 변경하는 함수
def toggle_color(self, msg):
    if 'bg-blue-500' in self.classes:
        self.set_class('bg-white')
    else:
        self.set_class('bg-blue-500')

# 메인 페이지 함수
def create_page():
    wp = jp.WebPage()
    
    # 요일을 표시하는 텍스트
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    # 전체 컨테이너 설정
    container = jp.Div(classes='bg-white p-4 shadow-lg rounded-lg', style='width: 320px;', a=wp)

    # 막대들을 담을 내부 컨테이너
    inner_container = jp.Div(classes='flex flex-col items-center', a=container)
    
    # 요일별 막대 컨테이너
    bars_container = jp.Div(classes='flex', a=inner_container)
    
    # 각 요일 막대 추가
    for day in days:
        day_container = jp.Div(classes='flex flex-col items-center mx-1', a=bars_container)
        jp.Div(text=day, classes='mb-2', a=day_container)
        bar = jp.Div(classes='w-8 h-48 border-2 border-gray-400 bg-white rounded', a=day_container)  
        bar.on('click', toggle_color) # 막대를 클릭하면 색상 바뀜

    return wp

