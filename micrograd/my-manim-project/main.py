from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.scale(0.5)
        circle.set_fill(RED,opacity=0.5)
        self.play(Create(circle))
        self.play(FadeOut(circle),subcaption="Hello")


class SquareToCircle(Scene):
    def construct(self):
        circle =Circle()
        circle.set_fill(BLUE,opacity=0.7)
        circle.scale(0.5)
        square = Square()
        square.set_fill(RED,opacity=0.7)
        square.scale(0.5)
        self.play(Create(square))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))




class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.scale(0.4)
        
        square = Square()
        square.set_fill(PINK, opacity=1)
        square.scale(0.4)

        square.next_to(circle,direction=UP, buff=0.2)
        self.play(Create(circle),Create(square))
        self.play(FadeOut(circle),FadeOut(square))


        
class RotateSquare(Scene):

    def construct(self):
        square = Square(color=GREEN).shift(LEFT * 0.5)
        square.scale(0.3)
        square2 = Square()
        square2.scale(0.3)
        square2.next_to(square,RIGHT,0.5)

        # self.play(Create(square),Create(square2))
        self.play(square.animate.rotate(PI),Rotate(square2,PI))
        self.wait(2)
