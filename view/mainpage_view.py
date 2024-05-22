import justpy as jp
from element.header import Header
from element.color import MainColors
from element.font import Font
from PyKakao import Local
from statics.button_theme import large_pill_button_classes, pill_button_classes, pill_button_style

def MainPageView():
    
    wp = jp.WebPage()
    head = Header("/")
    head.show_header(wp)
    
    main_colors = MainColors()
    font = Font()

    # Introduction Section
    intro_div = jp.Div(style=f'background-image: url(/static/statics/img/introduce.svg); height: auto; max-width: 100%; background-size: cover; display: flex; flex-direction: column; justify-content: center; align-items: center; line-height: 3;', classes=f'{font.Heading4_Regular}; text-center',children=[
        jp.P(text='　', classes='my-5', style='line-height: 0'),
        jp.P(text='일정 관리 플랫폼', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold};'),
        jp.P(text='　', classes='my-2', style='line-height: 0'),
        jp.P(text='여러 명의 사람들과 약속을 맞추는데 어려움을 겪으신 적이 없으신가요?', style=f'color: {main_colors.TextColor};'),
        jp.P(text='수많은 회의들을 관리하는데 불편하신 적이 없으신가요?', style=f'color: {main_colors.TextColor};'),
        jp.P(text='시간 뿐만 아니라 장소도 같이 정하기 귀찮지 않으셨나요?', style=f'color: {main_colors.TextColor};'),
        jp.Div(children=[
            jp.Span(text='여러 명의 사람들과 같이 협업하는 ', style=f'color: {main_colors.TextColor};'),
            jp.Span(text='PPP', style=f'color: {main_colors.MainColor};'), 
            jp.Span(text='가 함께하겠습니다', style=f'color: {main_colors.TextColor};'),
            jp.P(text='　', classes='my-10', style='line-height: 0'),
            jp.Div(classes='text-center', children=[
                jp.A(text="일정 계획하기", href="/signin", classes=f'{font.Heading2_Bold} text-center py-2 px-4 rounded-full', style=f'background-color: {main_colors.MainColor}; color: #FFFFFF; border-radius: 8px;')  # Added text-center class for center alignment
            ]),
        ])
    ])
    wp.add(intro_div)

    # Feature Section
    feature_div = jp.Div(classes='text-left relative', style=f'height: 180vh; margin-left: 40px; margin-right: 40px; display: flex; flex-direction: column; justify-content: center', children=[
        jp.P(text='약속과 장소를 한 번에', style=f'color: {main_colors.MainColor}', classes=f'{font.Heading2_Bold};'),
        jp.P(text='　', classes='my-2', style='line-height: 0'),
        jp.P(text='여러명과 여러개의', style='line-height: 0.8', classes=f'{font.Heading3_Bold}'), 
        jp.P(text='약속을 한번에!', classes=f'{font.Heading3_Bold}'),
        jp.P(text='　', classes='my-10', style='line-height: 15'),
        jp.P(text='약속을 편하게', style='line-height: 0.8; z-index: 2;', classes=f'{font.Heading3_Bold} text-right relative'),
        jp.P(text='잡아보세요', classes=f'{font.Heading3_Bold} text-right relative'),
        jp.Div(style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1;', children=[
            jp.Img(src='/static/statics/img/feature.svg', classes="mx-auto", style='height: auto; max-width: 100%;')
        ])
    ])
    
    wp.add(feature_div)

    
    # Usage Section
    usage_div = jp.Div(classes='text-center relative', style=f'background-color: {main_colors.GreyColor}; height: 180vh; display: flex; flex-direction: column; justify-content: center; align-items: center;', children=[
        jp.P(text='　', classes='my-10', style='line-height: 0'),
        jp.P(text='사용 방법', classes=f'{font.Heading3_Bold} text-center', style=f'color: {main_colors.TextColor};'),
        jp.P(text='　', classes='my-3', style='line-height: 0'),
        jp.Div(children=[
            jp.Span(text='간편하게 장소 및 일정 ', classes=f'{font.Heading2_Bold}'),
            jp.Span(text='약속 ', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold}'),
            jp.Span(text='만들기', classes=f'{font.Heading2_Bold}')
        ]),
        jp.P(text='　', classes='my-5', style='line-height: 0'),
        jp.P(text='일정과 장소를 여러명의 사람들과 한번에 정해보세요.', classes=f'{font.Small3}', style=f'color: {main_colors.TextColor};'),  
        jp.P(text='다양한 약속들을 잡을 수 있습니다.', classes=f'{font.Small3}', style=f'color: {main_colors.TextColor};'),  
        jp.P(text='　', classes='my-10', style='line-height: 30'),
        jp.P(text='Copyright 2021. PPP & UntoC CI.All right reserved.', classes=f'{font.Body1_Regular}'),
        jp.Div(style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 1;', children=[
            jp.Img(src='/static/statics/img/usage.svg', classes="mx-auto", style='height: auto; max-width: 100%;')
        ])
        
    ])
    wp.add(usage_div)
    
    return wp