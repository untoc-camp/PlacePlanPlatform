import justpy as jp
from element.header import Header
from element.color import MainColors
from element.font import Font
#from PyKakao import Local
from statics.button_theme import large_pill_button_classes, pill_button_classes, pill_button_style

def TimePromiseMapView():
    wp = jp.WebPage()
    header = Header("/timepromise/map")
    header.show_header(wp)
    
    main_colors = MainColors()
    font = Font()

    main_div = jp.Div(classes='flex flex-col', style=f'color: {main_colors.GreyColor}; height: 100vh; margin-left: 40px; margin-right: 40px; margin-top: 20px;', children=[
        jp.Div(style='margin-bottom: auto;', children=[
            jp.P(text='제목이 들어갈 공간입니다.', style='line-height: 0.8', classes=f'{font.Heading2_Bold}'), 
            jp.P(text='주최자: "언톡"', style='line-height: 0.8', classes=f'{font.Heading3_Bold}'), 
            jp.P(text='약속 종류: "미정"', style='line-height: 0.8', classes=f'{font.Heading3_Bold}')
        ]),
        jp.Div(style='display: flex;', children=[
            jp.Div(style='width: 50%;', children=[
                jp.P(text='약속 장소 : 부산 금정구 부산대학로83번길 2 (우)46241', style='line-height: 3', classes=f'{font.Heading3_Bold};'),
                jp.P(text='약속 장소 : 부산 금정구 부산대학로83번길 2 (우)46241', style='line-height: 3', classes=f'{font.Heading3_Bold}')
            ]),
            jp.Div(style='width: 50%;', children=[
                # Add the Kakao Map HTML file
                jp.Iframe(src='/static/statics/js/map.html', style='height: 500px; width: 100%; border: none;')
            ])
        ])
    ])
    wp.add(main_div)

    return wp
