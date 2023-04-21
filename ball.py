from shape import Shape
 
class Ball(Shape):
    def __init__(self, xcor=Screen().width/2, ycor=Screen().height/2, color = WHITE, x_vel = 5, y_vel = 4, radius=12):
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.max_y_vel = y_vel
        self.radius = radius
        super().__init__(xcor, ycor, color, sqrt(x_vel**2+y_vel**2))