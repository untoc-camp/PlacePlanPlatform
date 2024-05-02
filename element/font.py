
from element.color import MainColors


class Font:
    def __init__ (self):
        self.color = MainColors()
        self.Heading1_Bold = " font-bold text-5xl text-gray-800 mb-4 "
        self.Heading1_Regular = " text-5xl text-gray-800 "
        self.Heading2_Bold = " font-bold text-4xl text-gray-800 mb-4 "
        self.Heading2_Regular = " text-4xl text-gray-800 "
        self.Heading3_Bold = " font-bold text-3xl text-gray-800 mb-4 "
        self.Heading3_Regular = " text-3xl text-gray-800 "
        self.Heading4_Bold = " font-bold text-2xl text-gray-800 mb-4 "
        self.Heading4_Regular = " text-2xl text-gray-800 "
        
        self.Body1_Bold = " font-bold text-base text-gray-800 "
        self.Body1_Regular = " text-base text-gray-800 "
        self.Body2_Bold = " font-bold text-sm text-gray-800 "
        self.Body2_Regular = " text-sm text-gray-800 "
        
        self.Small1_Bold = " font-bold text-xs text-gray-800 "
        self.Small1_Regular = " text-xs text-gray-800 "
        self.Small2_Bold = " font-bold text-2xs text-gray-800 "
        self.Small2_Regular = " text-2xs text-gray-800 "
        self.Small3 = " text-3xs text-gray-800 "