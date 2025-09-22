from manim import *
class GridCirclesToLineSquares(Scene):
    def construct(self):
        rows, cols = 10, 10
        circle_spacing = 0.7   # spacing for circles grid
        square_side = 0.3      # size of final squares
        left_shift = -6        # shift final line to the left
        circles = VGroup()
        target_squares = []

        # --- Step 1: Circles in 10x10 grid ---
        circles = VGroup()  # <- group all circles so we can animate/position them easily
        for i in range(rows):
            for j in range(cols):
                x = j * circle_spacing - (cols-1) * circle_spacing / 2
                y = (rows-1) * circle_spacing / 2 - i * circle_spacing
                circle = Circle(radius=square_side/2)
                circle.set_fill(BLUE, opacity=0.6)
                circle.set_stroke(width=0)
                circle.move_to([x, y, 0])
                circles.add(circle)

        # animate the grid appearing
        # self.play(Create(circles), run_time=1.5)  # or use LaggedStart if you want a staggered effect

        # create the text and place it below the grid, then write it
        # text = Text("TEST", font_size=36).next_to(circles, UP, buff=0.5)
        # self.play(Write(text))
        # self.wait(0.1)

        # --- Step 2: Target squares in a single row ---
        for k in range(rows * cols):
            x = k * square_side + -10
            y = 0
            square = Square(side_length=square_side)
            square.set_fill(PURPLE, opacity=0.9)
            square.set_stroke(width=0)
            square.move_to([x, y, 0])
            target_squares.append(square)

        # Animate: show circles grid
        self.play(LaggedStartMap(Create, circles, lag_ratio=0.02))
        self.wait(3)

        # Animate: transform circles into line of squares
        self.play(
            LaggedStart(
                *[Transform(c, s) for c, s in zip(circles, target_squares)],
                lag_ratio=0.1,
                run_time=3
            )
        )
        self.wait()
