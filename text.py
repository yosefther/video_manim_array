from manim import *

class TextColorExample(Scene):
    def construct(self):  
        array_text = Text('Array', gradient=(BLUE, GREEN)).scale(3)
        var_text = Text('Variables', gradient=(BLUE, PURPLE)).scale(3)
        self.play(Write(var_text))
        self.wait(10)
