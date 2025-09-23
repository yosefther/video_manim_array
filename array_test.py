
from manim import *

class ArrayScene(Scene):
    def construct(self):
        values = [1, 2, 3, 4, 5]        
        in_total = 1.2                  
        hold_time = 1.6                 
        out_total = 1.2                 
        box_size = 1.0
        box_buff = 0.2
        font_size = 48
        #  boxes and labels
        boxes = VGroup(*[
            Square(side_length=box_size).set_stroke(width=2).set_fill(BLUE, opacity=0.1)
            for _ in values
        ]).arrange(RIGHT, buff=box_buff)

        labels = VGroup(*[
            Text(str(v), font_size=font_size).move_to(box)
            for v, box in zip(values, boxes)
        ])

        elements = VGroup(*[VGroup(b, l) for b, l in zip(boxes, labels)])
        elements.move_to(ORIGIN)

        # todo : index labels under the boxes does not working "fix latter"
        # indices = VGroup(*[
        #     Text(str(i), font_size=24).next_to(box, DOWN, buff=0.15)
        #     for i, box in enumerate(boxes)
        # ])
        # indices.move_to(ORIGIN)  # they follow the boxes by virtue of being positioned relative to them

        # IN animation: staggered FadeIn with a small overlap (lag_ratio)
        in_anim = LaggedStart(*[FadeIn(elem, shift=UP*0.3) for elem in elements], lag_ratio=0.2, run_time=in_total)
        self.play(in_anim)


        # hold on screen for the requested duration
        self.wait(hold_time)

        # OUT animation: staggered FadeOut in reverse order for nicer effect (numbers + boxes together)
        out_anim = LaggedStart(*[FadeOut(elem, shift=DOWN*0.3) for elem in reversed(elements)], lag_ratio=0.2, run_time=out_total)
        self.play(out_anim)


        self.wait(0.05)
