import math
from manim import *

class Taylor(Scene):
    def construct(self):

        title = Text("Taylor Series", font="Montserrat").scale(1.5).to_edge(UP).center()

        formula = (
            MathTex(r"f(x) = f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \cdots + \frac{f^{(n)}(x_0)}{n!}(x-x_0)^n")
                .scale(0.60)
        )

        formula_1 = MathTex(r"f(x) = \sum_{k = 0}^n \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k").scale(0.60)

        formula_2 = MathTex(r"sin(x) = \sum_{k = 0}^\infty (-1)^k \frac{x^{2k+1}}{(2k+1)!}").scale(0.60)

        all_formulas = VGroup(title, formula, formula_1, formula_2).arrange(DOWN, buff=0.5)

        self.add(all_formulas)
        self.wait(2)

        self.play(FadeOut(all_formulas))

        ax = Axes(
            x_range=[-15, 15],
            y_range=[-7, 7],
            x_length=20,
            y_length=15,
            axis_config={
                "include_ticks": False,
                "tip_shape": None,
                "stroke_width": 0.75,
            }
        )

        func = ax.plot(lambda x: np.sin(x), color=BLUE)

        ax.add(func)

        self.play(Write(ax))
        self.wait(2)

        def taylor_series (n):
            return lambda x:  sum([(-1)**k * x**(2*k + 1) / math.factorial(2*k + 1) for k in range(n)])

        taylor = ax.plot(taylor_series(0), color=GREEN)

        label = MathTex(r"n = 0").scale(0.60).to_edge(UL)

        self.add(label)

        for _ in range(1,13):
            self.play(
                Transform(taylor, ax.plot(taylor_series(_), color=GREEN, x_range=[-4 * PI, 4 * PI])),
                Transform(label, MathTex(r"n = " + str(_)).scale(0.60).to_edge(UL)),
                run_time=1
            )
            self.wait(1)