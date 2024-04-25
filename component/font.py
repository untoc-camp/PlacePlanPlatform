
from component.color import MainColors


class Font:
    def __init__ (self):
        self.color = MainColors()
        self.Heading1_Bold = "text-5xl font-bold"
        self.Heading1_Regular = "text-5xl"
        self.Heading2_Bold = "text-4xl font-bold"
        self.Heading2_Regular = "text-4xl"
        self.Heading3_Bold = "text-3xl font-bold"
        self.Heading3_Regular = "text-3xl"
        self.Heading4_Bold = "font-bold text-2xl text-gray-600 mb-4"
        self.Heading4_Regular = "text-2xl"
        
        self.Body1_Bold = "text-base font-bold"
        self.Body1_Regular = "text-base"
        self.Body2_Bold = "text-sm font-bold"
        self.Body2_Regular = "text-sm"
        
        self.Small1_Bold = "text-xs font-bold"
        self.Small1_Regular = "text-xs"
        self.Small2_Bold = "text-2xs font-bold"
        self.Small2_Regular = "text-2xs"
        self.Small3 = "text-3xs"