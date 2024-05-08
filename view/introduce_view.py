import justpy as jp
from element.header import Header
from element.color import MainColors
from element.font import Font

def IntroduceView():
    wp = jp.WebPage()
    head = Header("/introduce")
    head.show_header(wp)
    
    main_colors = MainColors()
    font = Font()
    # Introduction Section
    
    intro_div = jp.Div(classes='text-center',children=[
        jp.P(text='　', classes='my-4'),
        jp.P(text='일정 관리 플랫폼', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold}'),
        jp.P(text='　', classes='my-10'),
        jp.P(text='여러 명의 사람들과 약속을 맞추는데 어려움을 겪으신 적이 없으신가요?', classes=f'{font.Heading4_Regular} leading-loose', style=f'color: {main_colors.TextColor};'),
        jp.P(text='수많은 회의들을 관리하는데 불편하신 적이 없으신가요?', classes=f'{font.Heading4_Regular} leading-loose', style=f'color: {main_colors.TextColor};'),
        jp.P(text='시간 뿐만 아니라 장소도 같이 정하기 귀찮지 않으셨나요?', classes=f'{font.Heading4_Regular} leading-loose', style=f'color: {main_colors.TextColor};'),
        jp.Div(classes='text-center leading-loose', children=[
            jp.Span(text='여러 명의 사람들과 같이 협업하는 ', classes=f'{font.Heading4_Regular} ', style=f'color: {main_colors.TextColor};'),
            jp.Span(text='PPP', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading4_Bold}'), 
            jp.Span(text='가 함께하겠습니다', classes=f'{font.Heading4_Regular}', style=f'color: {main_colors.TextColor};')
        ]),
        jp.P(text='　', classes='my-20')
    ])
    
    # Action Button
    action_div = jp.Div(style=f'color: {main_colors.MainColor};', classes='text-center', children=[
        jp.A(text="일정 계획하기", href="/signin", classes=f'{font.Heading2_Bold} text-center', style=f"color: #000000")  # Added text-center class for center alignment
    ])

    # Feature Section
    feature_div = jp.Div(classes='text-left', style=f'margin-left: 40px; margin-right: 40px;', children=[
        jp.P(text='　', classes='my-4'),
        jp.P(text='약속과 장소를 한 번에', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold} leading-normal'),
        jp.P(text='여러명과 여러개의', classes=f'{font.Heading3_Bold}'),
        jp.P(text='약속을 한번에!', classes=f'{font.Heading3_Bold}'),
        jp.P(text='　', classes='my-20'),
        jp.P(text='약속을 편하게', classes=f'{font.Heading3_Bold} text-right'),
        jp.P(text='잡아보세요', classes=f'{font.Heading3_Bold} text-right'),
        jp.P(text='　', classes='my-20')
    ])
    
    # Usage Section
    usage_div = jp.Div(classes='text-center leading-loose', style=f'background-color: {main_colors.GreyColor};', children=[
        jp.P(text='　', classes='my-10'),
        jp.P(text='사용 방법', classes=f'{font.Heading3_Bold} text-center', style=f'color: {main_colors.TextColor};'),
        jp.P(text='　', classes='my-5'),
        jp.Div(classes='text-center', children=[
            jp.Span(text='간편하게 장소 및 일정 ', classes=f'{font.Heading2_Bold}'),
            jp.Span(text='약속 ', style=f'color: {main_colors.MainColor};', classes=f'{font.Heading2_Bold}'),
            jp.Span(text='만들기', classes=f'{font.Heading2_Bold}')
        ]),
        jp.P(text='　', classes='my-5'),
        jp.P(text='일정과 장소를 여러명의 사람들과 한번에 정해보세요.', classes=f'{font.Body1_Regular}', style=f'color: {main_colors.TextColor};'),  
        jp.P(text='다양한 약속들을 잡을 수 있습니다.', classes=f'{font.Body1_Regular}', style=f'color: {main_colors.TextColor};'),  
        jp.P(text='　', classes='my-20'),
        jp.P(text='　', classes='my-20'),
        jp.P(text='Copyright 2021. PPP & UntoC cl.All right reserved.', classes=f'{font.Small3}'),
        jp.P(text='　', classes='my-20')  
    ])
    
    # Adding sections to the webpage
    wp.add(intro_div)
    wp.add(action_div)
    wp.add(feature_div)
    wp.add(usage_div)
    
    return wp