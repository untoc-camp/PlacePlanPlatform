import justpy as jp
from element.header import Header
from element.color import MainColors
from element.font import Font
import json

json_data = '''
{
    "title": "약속 제목",
    "organizer": "언톡",
    "promise_type": "미정",
    "location": "부산 금정구 부산대학로83번길 2 (우)46241"
}
'''

content_data = json.loads(json_data)

def TimePromiseMapView():
    wp = jp.WebPage()
    header = Header("/timepromise/map")
    header.show_header(wp)
    
    main_colors = MainColors()
    font = Font()

    main_div = jp.Div(classes='flex flex-col', style=f'color: {main_colors.GreyColor}; height: 100vh; margin-left: 40px; margin-right: 40px; margin-top: 20px;')
    
    # 타이틀 및 정보 출력
    jp.P(text=content_data["title"], style='line-height: 0.8', classes=f'{font.Heading2_Bold}', a=main_div)
    jp.P(text=f'주최자: {content_data["organizer"]}', style='line-height: 0.8', classes=f'{font.Heading3_Bold}', a=main_div)
    jp.P(text=f'약속 종류: {content_data["promise_type"]}', style='line-height: 0.8', classes=f'{font.Heading3_Bold}', a=main_div)

    # 장소 정보 및 지도 출력
    location_div = jp.Div(style='display: flex;', a=main_div)
    jp.Div(text=f'약속 장소: {content_data["location"]}', style='line-height: 3', classes=f'{font.Heading3_Bold}', a=location_div)
    jp.Iframe(src=f'/static/statics/js/map.html?location={json.dumps(content_data)}', style='height: 500px; width: 50%; border: none;', a=location_div)

    wp.add(main_div)

    return wp