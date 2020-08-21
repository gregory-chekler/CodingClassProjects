import turtle
import random
def main():
    t1 = turtle.Turtle()
    t1.pu()
    t2 = turtle.Turtle()
    t2.pu()
    t3 = turtle.Turtle()
    t3.pu()
    t4 = turtle.Turtle()
    t4.pu()
    t5 = turtle.Turtle()
    t5.pu()
    t6 = turtle.Turtle()
    t6.pu()

    racers = [t1, t2, t3, t4, t5, t6]
    
    pos = 100
    
    for r in racers:
        r.goto(-300, pos)
        pos -= 50
        
    finished = False
    while not finished:
        for r in racers:
            r.forward(random.randint(10, 20))
            if r.xcor() > 300:
                finished = True
    if finished:
        print("Your winner is: ", r)
main()