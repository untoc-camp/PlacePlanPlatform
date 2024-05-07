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

    wp.add(jp.P(text='.', classes='my-4'))
    wp.add(jp.P(text='일정 관리 플랫폼', classes=f'{font.Heading2_Bold} text-center'))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-10'))
    wp.add(jp.P(text='여러 명의 사람들과 약속을 맞추는데 어려움을 겪으신 적이 없으신가요?', classes=f'{font.Heading4_Regular} text-center leading-loose'))  # Added text-center class for center alignment
    wp.add(jp.P(text='수많은 회의들을 관리하는데 불편하신 적이 없으신가요?', classes=f'{font.Heading4_Regular} text-center leading-loose'))  # Added text-center class for center alignment
    wp.add(jp.P(text='시간 뿐만 아니라 장소도 같이 정하기 귀찮지 않으셨나요?', classes=f'{font.Heading4_Regular} text-center leading-loose'))  # Added text-center class for center alignment
    wp.add(jp.P(text='여러명의 사람들과 같이 협업하는 플랫폼 PPP가 함께하겠습니다', classes=f'{font.Heading4_Regular} text-center leading-loose'))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-20'))
    wp.add(jp.A(text="일정 계획하기", href="/signin", classes=f'{font.Heading2_Bold} text-center', style=f"color: {main_colors.MainColor};"))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-4'))
    wp.add(jp.P(text='약속과 장소를 한 번에', classes=f'{font.Heading2_Bold} text-left leading-normal'))  # Added text-center class for center alignment
    wp.add(jp.P(text='여러명과 여러개의', classes=f'{font.Heading3_Bold} text-left'))  # Added text-center class for center alignment
    wp.add(jp.P(text='약속을 한번에!', classes=f'{font.Heading3_Bold} text-left'))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-20'))
    wp.add(jp.P(text='약속을 편하게', classes=f'{font.Heading3_Bold} text-right'))  # Added text-center class for center alignment
    wp.add(jp.P(text='잡아보세요', classes=f'{font.Heading3_Bold} text-right'))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-20'))
    wp.add(jp.P(text='사용 방법', classes=f'{font.Heading3_Bold} text-center'))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-5'))
    wp.add(jp.P(text='간편하게 장소 및 일정 약속 만들기', classes=f'{font.Heading2_Bold} text-center'))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-5'))
    wp.add(jp.P(text='일정과 장소를 여러명의 사람들과 한번에 정해보세요.', classes=f'{font.Body1_Regular} text-center'))  # Added text-center class for center alignment
    wp.add(jp.P(text='다양한 약속들을 잡을 수 있습니다.', classes=f'{font.Body1_Regular} text-center'))  # Added text-center class for center alignment
    wp.add(jp.P(text='.', classes='my-20'))
    return wp
