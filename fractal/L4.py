import turtle
from random import randrange


class L4:
    def __init__(self):
        # screen settings
        self.width, self.height = 800, 800
        screen = turtle.Screen()
        screen.setup(self.width, self.height)
        screen.delay(0)
        screen.bgcolor('black')
        # pen settings
        self.pen = turtle.Turtle()
        self.pen.pensize(1)
        self.pen.speed(0)
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.setpos(0, -self.height // 2)
        self.pen.pendown()
        self.pen.color('green')
        turtle.hideturtle()
        # l-system settings
        self.ch1 = 'X'
        self.rules = {self.ch1: 'F[@[-X]+X]'}
        self.stack = []

    def apply_rule(self, axiom):
        return ''.join([self.rules.get(ch, ch) for ch in axiom])

    def get_gen(self, gen):
        axiom = 'X'
        for c in range(gen):
            axiom = self.apply_rule(axiom)
        return axiom

    def run(self):
        step, angle, color, thickness = 80, lambda: randrange(10, 45), (0.2, 0.2, 0.0), 30
        gen = 12
        turtle.color('white')
        turtle.goto(-self.width // 2 + 50, -self.height // 2 + 50)
        turtle.clear()
        turtle.write(f'gen: {gen}', font=('arial', 20, 'normal'))
        pen = self.pen
        print(self.get_gen(gen))
        pen.left(90)
        for ch in self.get_gen(gen):
            pen.pensize(thickness)
            pen.color(color)
            if ch in ['F', 'X']:
                pen.forward(step)
            elif ch == '@':
                step -= 5
                color = (color[0], color[1] + 0.04, color[2])
                thickness -= 3
                thickness = max(1, thickness)
            elif ch == '+':
                pen.right(angle())
            elif ch == '-':
                pen.left(angle())
            elif ch == '[':
                a, p = pen.heading(), pen.pos()
                self.stack.append((a, p, step, color, thickness))
            elif ch == ']':
                a, p, step, color, thickness = self.stack.pop()
                pen.setheading(a)
                pen.penup()
                pen.goto(p)
                pen.pendown()
        turtle.Screen().exitonclick()


if __name__ == '__main__':
    app = L4()
    app.run()
