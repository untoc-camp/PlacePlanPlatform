import justpy as jp

class Popup: #모든 선언은 example = Popup1(wp,"제목","내용") 꼴로 하시면 됩니다.
    def __init__(self, wp, popup_title='', popup_text=''):
        self.wp = wp
        self.dialog = jp.Div(classes="fixed inset-0 bg-gray-800 bg-opacity-50 items-center justify-center hidden", a=wp)
        self.dialog.show = False  # 처음에는 숨겨진 상태
        
        self.popup_content = jp.Div(classes="bg-white p-5 rounded-lg text-center", a=self.dialog)
        self.popup_title = jp.P(text=popup_title, classes="font-semibold mb-4", a=self.popup_content)
        self.popup_text = jp.P(text=popup_text, classes="mb-4", a=self.popup_content)

    def show_popup(self, msg):
        # 팝업을 보이게 설정
        self.dialog.show = True
        self.dialog.set_class('flex')

    def close_popup(self, msg):
        # 팝업을 숨기게 설정
        self.dialog.show = False
        self.dialog.set_class('hidden')

class Popup1(Popup): #확인 버튼만 존재하는 팝업입니다. (1개의 버튼이라서 Popup1)
    def __init__(self, wp, popup_title='', popup_text=''):
        super().__init__(wp, popup_title, popup_text)

        self.close_button = jp.Button(text='확인', classes='bg-blue-500 text-white p-2 rounded', style='border-radius: 8px', a=self.popup_content, click=self.close_popup)
        self.close_button.dialog = self.dialog  # 닫기 버튼과 팝업 다이얼로그 연결

class Popup2(Popup): #확인 버튼과 취소 버튼이 존재하는 팝업입니다. (2개의 버튼이라서 Popup2)
    def __init__(self, wp, popup_title='', popup_text=''):
        super().__init__(wp, popup_title, popup_text)
        
        # 버튼들을 담을 div
        self.button_div = jp.Div(classes="flex justify-center gap-4", a=self.popup_content)
        
        self.confirm_button = jp.Button(text='확인', classes='bg-blue-500 text-white p-2 rounded', style='border-radius: 8px', a=self.button_div, click=self.close_popup)
        self.cancel_button = jp.Button(text='취소', classes='bg-white text-blue-500 p-2 rounded border border-blue-500', style='border-radius: 8px', a=self.button_div, click=self.close_popup)
        
        self.confirm_button.dialog = self.dialog  # 버튼과 팝업 다이얼로그 연결
        self.cancel_button.dialog = self.dialog  # 버튼과 팝업 다이얼로그 연결

class PopupText(Popup): #확인 버튼과 placeholder가 존재하는 팝업입니다. (text를 작성할 수 있어서 PopupText)
    def __init__(self, wp, popup_title='', popup_text=''):
        super().__init__(wp, popup_title, popup_text)
        
        # 사용자 입력란 추가
        self.user_input = jp.Input(placeholder="내용을 입력해주세요.", classes="border p-2 mb-4 w-full", style="height: 100px;", a=self.popup_content)
        self.close_button = jp.Button(text='확인', classes='bg-blue-500 text-white p-2 rounded', style='border-radius: 8px', a=self.popup_content, click=self.close_popup)
        self.close_button.dialog = self.dialog  # 닫기 버튼과 팝업 다이얼로그 연결