from turtle import *
color('red', 'yellow')

def flower(size, petals):
    for i in range(petals):
        circle(size)
        left(360/petals)

flower(100, 7)



done()