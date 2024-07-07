"""from turtle import *
import colorsys 

tracer(100)
bgcolor('black')
pensize(20)
h=0.6
up()
goto(-150, 0)
down()

for i in range(500):
    c=colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.001
    color(c)
    up(), circle(i, 20)
    down(), circle(65,145)
    lt(141)
done()
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
import colorsys

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.h = 0.6
        with self.canvas:
            self.draw_pattern()

    def draw_pattern(self):
        for i in range(500):
            rgb = colorsys.hsv_to_rgb(self.h, 1, 1)
            self.h += 0.001
            Color(*rgb)
            self.circle_line(i, 20)
            self.circle_line(65, 145)
    
    def circle_line(self, radius, angle):
        # This function approximates a circle using lines
        import math
        segments = 360 // angle
        points = []
        for i in range(segments + 1):
            theta = math.radians(i * angle)
            x = self.center_x + radius * math.cos(theta)
            y = self.center_y + radius * math.sin(theta)
            points += [x, y]
        Line(points=points, width=2)

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
