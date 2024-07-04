import justpy as jp
from element.header import Header
from element.color import MainColors
from element.font import Font
import json

def TimePromiseMapView():
    wp = jp.WebPage()
    header = Header("/timepromise/map")
    header.show_header(wp)
    
    main_colors = MainColors()
    font = Font()

    with open('data/location.json', 'r', encoding='utf-8') as file:
        content_data = json.load(file)[0]


    main_div = jp.Div(classes='flex flex-col', style=f'color: {main_colors.GreyColor}; height: 100vh; margin-left: 40px; margin-right: 40px; margin-top: 20px;')
    jp.Div(text=f'약속 장소: {content_data["location"]}', style='line-height: 3', classes=f'{font.Heading3_Bold}', a=main_div)

    # 장소 정보 및 지도 출력
    location_div = jp.Div(style='display: flex;', a=main_div)
    jp.Iframe(src=f'/static/statics/js/map.html?location={jp.quote(json.dumps(content_data))}', style='height: 500px; width: 50%; border: none;', a=location_div)

    wp.add(main_div)

    return wp

#이 파일은 통째로 삭제 예정, 근시일 내에 time_promise_detail_view.py로 이동될 예정임. (진행 상황 고려 후 통합)