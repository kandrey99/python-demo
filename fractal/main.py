import turtle

WIDTH, HEIGHT = 1000, 800
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
pen = turtle.Turtle()

chr_1, rule_1 = 'A', 'AB'
chr_2, rule_2 = 'B', 'A'
step = 10
angle = 60
gen = 10


def apply_rule(axiom):
    return ''.join([rule_1 if ch == chr_1 else rule_2 for ch in axiom])


def main():
    turtle.penup()
    turtle.goto(-WIDTH//2+50, -HEIGHT//2+50)
    turtle.write('test',  font=('arial', 30))
    turtle.Screen().exitonclick()


if __name__ == '__main__':
    main()
