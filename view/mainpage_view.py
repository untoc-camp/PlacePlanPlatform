import justpy as jp
from element.header import Header
from element.color import MainColors
from element.font import Font

def MainPageView():
    
    wp = jp.WebPage()
    head = Header("/introduce")
    head.show_header(wp)
    
    main_colors = MainColors()
    font = Font()

    # Introduction Section
    intro_div = jp.Div(style=f'background-image: url(/static/statics/img/main.jpg); background-size: cover; display: flex; flex-direction: column; justify-content: center; align-items: center;', classes=f'{font.Heading4_Regular}; text-center leading-loose',children=[
        jp.P(text='　', classes='my-4'),
        jp.P(text='일정 관리 플랫폼', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold}'),
        jp.P(text='　', classes='my-10'),
        jp.P(text='여러 명의 사람들과 약속을 맞추는데 어려움을 겪으신 적이 없으신가요?', style=f'color: {main_colors.TextColor};'),
        jp.P(text='수많은 회의들을 관리하는데 불편하신 적이 없으신가요?', style=f'color: {main_colors.TextColor};'),
        jp.P(text='시간 뿐만 아니라 장소도 같이 정하기 귀찮지 않으셨나요?', style=f'color: {main_colors.TextColor};'),
        jp.Div(children=[
            jp.Span(text='여러 명의 사람들과 같이 협업하는 ', style=f'color: {main_colors.TextColor};'),
            jp.Span(text='PPP', style=f'color: {main_colors.MainColor};'), 
            jp.Span(text='가 함께하겠습니다', style=f'color: {main_colors.TextColor};'),
            jp.P(text='　', classes='my-10'),
            jp.Div(classes='text-center', children=[
                jp.A(text="일정 계획하기", href="#feature", classes=f'{font.Heading2_Bold} text-center', style=f'background-color: {main_colors.MainColor}; color: #FFFFFF')  # Added text-center class for center alignment
            ]),
        ]),
        jp.P(text='　', classes='my-10')
    ])
    wp.add(intro_div)

    # Feature Section
    feature_div = jp.Div(classes='text-left', style=f'margin-left: 40px; margin-right: 40px; display: flex; flex-direction: column; justify-content: center; align-items: center;', children=[
        jp.P(text='　', classes='my-4'),
        jp.P(text='약속과 장소를 한 번에', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold} leading-normal', id="feature"),
        jp.P(text='여러명과 여러개의', classes=f'{font.Heading3_Bold}'),
        jp.P(text='약속을 한번에!', classes=f'{font.Heading3_Bold}'),
        jp.Div(classes='text-center', children=[
            jp.Img(src='/static/statics/img/usage.png', classes = "mx-auto", style='height: 500px; width: auto;')
        ]), 
        jp.P(text='약속을 편하게', classes=f'{font.Heading3_Bold} text-right'),
        jp.P(text='잡아보세요', classes=f'{font.Heading3_Bold} text-right'),
        jp.P(text='　', classes='my-20')
    ])
    wp.add(feature_div)
    
    # Usage Section
    usage_div = jp.Div(classes='text-center leading-loose', style=f'background-color: {main_colors.GreyColor}; display: flex; flex-direction: column; justify-content: center; align-items: center;', children=[
        jp.P(text='　', classes='my-10'),
        jp.P(text='사용 방법', classes=f'{font.Heading3_Bold} text-center', style=f'color: {main_colors.TextColor};'),
        jp.P(text='　', classes='my-5'),
        jp.Div(children=[
            jp.Span(text='간편하게 장소 및 일정 ', classes=f'{font.Heading2_Bold}'),
            jp.Span(text='약속 ', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold}'),
            jp.Span(text='만들기', classes=f'{font.Heading2_Bold}')
        ]),
        jp.P(text='　', classes='my-5'),
        jp.P(text='일정과 장소를 여러명의 사람들과 한번에 정해보세요.', classes=f'{font.Small3}', style=f'color: {main_colors.TextColor};'),  
        jp.P(text='다양한 약속들을 잡을 수 있습니다.', classes=f'{font.Small3}', style=f'color: {main_colors.TextColor};'),  
        jp.P(text='　', classes='my-10'),
        jp.Div(classes='text-center', children=[
            jp.Img(src='/static/statics/img/howtouse.png', classes = "mx-auto", style='height: 300px; width: auto;')
        ]),
        jp.P(text='　', classes='my-20'),
        jp.P(text='Copyright 2021. PPP & UntoC cl.All right reserved.', classes=f'{font.Body1_Regular}'),
        jp.P(text='　', classes='my-20')  
    ])
    wp.add(usage_div)

    return wp

# Run the app
jp.justpy(MainPageView)
