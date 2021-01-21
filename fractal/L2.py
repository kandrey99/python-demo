import turtle


class L2:
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
        self.pen.setpos(-self.width // 2, -self.height // 2)
        self.pen.pendown()
        self.pen.color('orange')
        turtle.hideturtle()
        # l-system settings
        self.ch1, self.ch2 = 'F', 'G'
        self.rules = {self.ch1: 'F-G+F+G-F', self.ch2: 'GG'}

    def apply_rule(self, axiom):
        return ''.join([self.rules.get(ch, ch) for ch in axiom])

    def get_gen(self, gen):
        axiom = 'F'
        for c in range(gen):
            axiom = self.apply_rule(axiom)
        return axiom

    def run(self):
        step, angle = 16, 120
        turtle.goto(-self.width // 2 + 50, self.height // 2 - 50)
        turtle.clear()
        gen = 6
        turtle.write(f'gen: {gen}', font=('arial', 20, 'normal'))
        pen = self.pen
        print(self.get_gen(gen))
        for ch in self.get_gen(gen):
            if ch == self.ch1 or ch == self.ch2:
                pen.forward(step)
            elif ch == '+':
                pen.right(angle)
            else:
                pen.left(angle)
        turtle.Screen().exitonclick()


if __name__ == '__main__':
    app = L2()
    app.run()
