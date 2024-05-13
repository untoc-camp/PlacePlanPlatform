
from element.color import MainColors
from element.font import Font


color = MainColors()
font = Font()

#이렇게 사용하시면 됩니다
#large는 로그인에서 쓰는 큰버튼 디폴트 값입니다.
#jp.Button(text="Click me", a=wp, style= pill_button_style() , classes=large_pill_button_classes())

def pill_button_classes(width = 8, height = 2):
    return f"text-white py-{height} px-{width} rounded-full {font.Body1_Bold} text-center"

def pill_button_style():
    return f"background-color: {color.MainColor}; color: #FFFFFF; border-radius: 10px;"

def large_pill_button_classes(width = 60, height = 8):
    return f"text-white py-{height} px-{width} rounded-full {font.Heading3_Bold} text-center"