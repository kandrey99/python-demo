import turtle


class L3:
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
        self.pen.setpos(self.width // 2 - 150, -self.height // 2 + 100)
        self.pen.pendown()
        self.pen.color('orange')
        turtle.hideturtle()
        # l-system settings
        self.ch1, self.ch2 = 'X', 'Y'
        self.rules = {self.ch1: 'X+YF+', self.ch2: '-FX-Y'}

    def apply_rule(self, axiom):
        return ''.join([self.rules.get(ch, ch) for ch in axiom])

    def get_gen(self, gen):
        axiom = 'XY'
        for c in range(gen):
            axiom = self.apply_rule(axiom)
        return axiom

    def run(self):
        step, angle = 4, 90
        turtle.color('white')
        turtle.goto(-self.width // 2 + 50, self.height // 2 - 50)
        turtle.clear()
        gen = 13
        turtle.write(f'gen: {gen}', font=('arial', 20, 'normal'))
        pen = self.pen
        print(self.get_gen(gen))
        for ch in self.get_gen(gen):
            if ch == self.ch1 or ch == self.ch2:
                pen.forward(step)
            elif ch == '+':
                pen.right(angle)
            elif ch == '-':
                pen.left(angle)
        turtle.Screen().exitonclick()


if __name__ == '__main__':
    app = L3()
    app.run()
