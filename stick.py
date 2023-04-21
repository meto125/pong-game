from shape import Shape
        
class Stick(Shape):
    def __init__(self, xcor, ycor, color = WHITE, width=15, height=120,real_velocity=4):
        self.width = width
        self.height = height
        super().__init__(xcor, ycor, color, real_velocity)