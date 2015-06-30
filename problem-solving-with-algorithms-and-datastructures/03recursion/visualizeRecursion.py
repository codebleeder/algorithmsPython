__author__ = 'cloudera'
import turtle


def draw_spiral(my_turtle, length):
    if length > 0:
        my_turtle.forward(length)
        my_turtle.right(90)
        draw_spiral(my_turtle, length-5)


def tree(t, branch):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        tree(t, branch-15)
        t.left(40)
        tree(t, branch-15)
        t.right(20)
        t.backward(branch)


def main():
    my_turtle = turtle.Turtle()
    my_window = turtle.Screen()
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color('green')
    tree(my_turtle, 75)
    my_window.exitonclick()


main()