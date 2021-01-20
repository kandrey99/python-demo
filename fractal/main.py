import turtle

# screen settings
WIDTH, HEIGHT = 800, 800
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.delay(0)
# pen settings
pen = turtle.Turtle()
pen.pensize(1)
pen.speed(0)
pen.hideturtle()
turtle.hideturtle()

chr_1, rule_1 = 'A', 'AB'
chr_2, rule_2 = 'B', 'A'
step = 20
angle = 60
gens = 100


def apply_rule(axiom):
    return ''.join([rule_1 if ch == chr_1 else rule_2 for ch in axiom])


def get_gen(gen):
    axiom = 'A'
    for c in range(gen):
        axiom = apply_rule(axiom)
    return axiom


def main():
    gen = 20
    turtle.goto(-WIDTH // 2 + 50, -HEIGHT // 2 + 50)
    turtle.clear()
    turtle.write(f'gen: {gen}', font=('arial', 20, 'normal'))
    pen.setheading(0)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.clear()
    for c in get_gen(gen):
        pen.forward(step)
        pen.left(angle) if c == chr_1 else pen.right(angle)
        pen.forward(step)
        pen.left(angle) if c == chr_1 else pen.right(angle)


if __name__ == '__main__':
    main()
