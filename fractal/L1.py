import turtle


class L1:
    def __init__(self):
        # screen settings
        self.width, self.height = 800, 800
        screen = turtle.Screen()
        screen.setup(self.width, self.height)
        screen.delay(0)
        # pen settings
        self.pen = turtle.Turtle()
        self.pen.pensize(1)
        self.pen.speed(0)
        self.pen.hideturtle()
        turtle.hideturtle()
        # l-system settings
        self.chr_1, self.rule_1 = 'A', 'AB'
        self.chr_2, self.rule_2 = 'B', 'A'

    def apply_rule(self, axiom):
        return ''.join([self.rule_1 if ch == self.chr_1 else self.rule_2 for ch in axiom])

    def get_gen(self, gen):
        axiom = 'A'
        for c in range(gen):
            axiom = self.apply_rule(axiom)
        return axiom

    def run(self):
        step = 20
        angle = 60
        gen = 20
        turtle.goto(-self.width // 2 + 50, -self.height // 2 + 50)
        turtle.clear()
        turtle.write(f'gen: {gen}', font=('arial', 20, 'normal'))
        pen = self.pen
        pen.setheading(0)
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.clear()
        for c in self.get_gen(gen):
            pen.forward(step)
            pen.left(angle) if c == self.chr_1 else pen.right(angle)
            pen.forward(step)
            pen.left(angle) if c == self.chr_1 else pen.right(angle)


if __name__ == '__main__':
    app = L1()
    app.run()
