import math
import turtle


def input_radius():
    rad = float(input("Nceda ufake uququzelelo y:"))
    return rad


def calc_area(rad):
    a = math.pi * rad * rad
    return a


def calc_perimeter(rad):
    peri = 2 * math.pi * rad
    return peri


if __name__ == '__main__':
    radius = input_radius()
    t = turtle.Turtle()
    t.circle(50)
    print("indawo yesangqa:", calc_area(radius))
    print("Iparameter:", calc_perimeter(radius))