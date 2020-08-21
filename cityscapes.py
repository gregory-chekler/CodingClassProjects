#!/usr/bin/python
#cityscapes.py
'''Creates a city and runs a race between two vehicles'''
__author__ = "Gregory Chekler"
__version__ = "1.0.0"


import turtle
import time
import random
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape



def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width = 1.0, height = 1.0)
    t.ht()
    t.pu()
    
    
    #######################
    # UI and Input Interface
    ########################
    
    t.write("Hello! Welcome to Gregory Chekler's cityscapes simulation", True,
            "center", font =
             ("Verdana", 18, "normal"))
    answer = screen.textinput("yes or No", "Are you ready to start?")
    if answer != "yes":
        t.undo()
        t.write("See you later!", True, "center", font =
             ("Verdana", 18, "normal"))
    else:
        t.undo()
        t.write("Awesome!!!", True, "center", font =
             ("Verdana", 18, "normal"))
        t.undo()
        bdg = int(screen.textinput("Number", "How many buildings do you want?"))
        screen.setup(width = 1.0, height = 1.0)
        ws = float(screen.window_width())
        
        screen = turtle.Screen()
        screen.setup(width = 1.0, height = 1.0)
        screen.tracer(2)
        t.speed(9)

#Creates the stary night background
        s = turtle.Screen()
        s.register_shape("giphy.gif")
        turt = turtle.Turtle()
        turt.shape("giphy.gif")
        turt.pensize(80)
        larger_turt = PhotoImage(file="giphy.gif").zoom(6, 6)
        screen.addshape("larger_turt", Shape("image", larger_turt))
        turt = Turtle("larger_turt")
        turt.penup()
        turt.st()
        turt.stamp()
        
        
        bdg_w = (ws // bdg)
        t.goto(-1 * ws // 2, 0)#Used for setting up turtles at left of screen
        t.ht()
        t.down()
        t.pensize(3)
        t.shape("turtle")
        screen.colormode(255) #creates random color buildings
        t.ht()
        area = 0
        
        #Creates buildings
        for i in range(bdg): 
            t.ht()
            t.down()
            height = int(random.randint(100, 300))
            t.color("Black")
            t.begin_fill()
            t.lt(90)
            t.forward(height)
            t.rt(90)
            t.fd(ws // bdg)
            t.rt(90)
            t.forward(height)
            t.rt(90)
            t.forward(ws // bdg)
            t.right(180)
            t.forward(ws // bdg)
            t.color(random.randrange(256), random.randrange(256),
                    random.randrange(256)) #building color
            t.end_fill()
            t.up()
            t.ht()
            area = height * bdg_w + area
        
        #Determines area of all the buildings
        area = str(area)
        wrt = turtle.Turtle()
        wrt_sc = turtle.Screen()
        wrt_sc.tracer(2)
        wrt.speed(9)
        wrt.ht()
        wrt.penup()
        wrt.color("white")
        wrt.goto(0, -275)
        wrt.pendown()
        wrt.write("The total area is: " + area + " square feet!", True, "center", font =
                    ("Verdana", 18, "normal"))
        time.sleep(2)
        wrt.undo()
        
        t.goto(-1 * ws // 2, 0) #Door number functions
        t.up()
        t.pensize(3)
        t.color("Black")
        door_number = int(3 + bdg)
        
        for door in range(bdg): #Creates doors
            t.pendown()
            t.forward(30)
            t.left(90)
            t.fd(20)
            t.left(90)
            t.forward(30)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(10)
            door_number = door_number + 2
            t.write(door_number, True, "center", font =
             ("Verdana", 12, "normal"))
            t.backward(14)
            t.penup()
            t.forward(bdg_w)
            
        
        
        #########################
        # Builds the street
        #########################
        t.goto(-1 * ws // 2, 0) #Lane 1
        t.pendown()
        t.pensize(3)
        t.color("Black")
        t.begin_fill()
        t.setheading(0)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(ws)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(ws)
        t.left(90)
        color = "grey"
        t.color(color)
        t.end_fill()
           
        t.goto(-1 * ws // 2, -100)#Stripe
        t.pendown()
        t.pensize(3)
        t.color("Black")
        t.begin_fill()
        t.setheading(0)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(ws)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(ws)
        t.left(90)
        color = "yellow"
        t.color(color)
        t.end_fill()
          
        t.goto(-1 * ws // 2, -120) #Marker
        t.pendown()
        t.pensize(3)
        t.color("Black")
        t.begin_fill()
        t.setheading(0)
        t.right(90)
        t.forward(5)
        t.left(90)
        t.forward(ws)
        t.left(90)
        t.forward(5)
        t.left(90)
        t.forward(ws)
        t.left(90)
        color = "black"
        t.color(color)
        t.end_fill()
           
        t.goto(-1 * ws // 2, -125)#second stripe
        t.pendown()
        t.pensize(3)
        t.color("Black")
        t.begin_fill()
        t.setheading(0)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(ws)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(ws)
        t.left(90)
        color = "yellow"
        t.color(color)
        t.end_fill()
          
        t.goto(-1 * ws // 2, -145) # second lane
        t.pendown()
        t.pensize(3)
        t.color("Black")
        t.begin_fill()
        t.setheading(0)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(ws)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(ws)
        t.left(90)
        color = "grey"
        t.color(color)
        t.end_fill()
        
        t.goto(-1 * ws // 2, -245) #ocean
        t.pendown()
        t.pensize(3)
        t.color("Black")
        t.begin_fill()
        t.setheading(0)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(ws)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(ws)
        t.left(90)
        color = "Blue"
        t.color(color)
        t.end_fill()
        
        #Car
        s.register_shape("car.gif")
        larger = PhotoImage(file = "car.gif").subsample(3, 3)
        screen.addshape("larger", Shape("image", larger))
        car_one = Turtle("larger")
        car_one.penup()
        car_one.st()
        car_one.goto(-600, -50)
        
        #Bus
        s.register_shape("bus.gif")
        larger_two = PhotoImage(file = "bus.gif").subsample(6, 6)
        screen.addshape("larger_two", Shape("image", larger_two))
        car_two = Turtle("larger_two")
        car_two.penup()
        car_two.st()
        car_two.goto(-600, -192)
        screen.tracer(1)
        t.speed(1)
        
        #Count down to race
        wrt = turtle.Turtle()
        wrt_sc = turtle.Screen()
        wrt_sc.tracer(2)
        wrt.speed(9)
        wrt.ht()
        wrt.penup()
        wrt.color("White")
        wrt.goto(0, -275)
        wrt.pendown()
        wrt.write("3...", True, "center", font =
            ("Verdana", 18, "normal"))
        time.sleep(1)
        wrt.undo()
        wrt.write("2...", True, "center", font =
            ("Verdana", 18, "normal"))
        time.sleep(1)
        wrt.undo()
        wrt.write("1...", True, "center", font =
            ("Verdana", 18, "normal"))
        time.sleep(1)
        wrt.undo()
        wrt.write("Go!!!", True, "center", font =
            ("Verdana", 18, "normal"))
        time.sleep(1)
        wrt.undo()
        

#####################
# Racing function
####################

        while car_one.xcor() < 600:            
            caronerand = random.randint(1, 10)
            cartworand = random.randint(1, 10)
            car_one.fd(caronerand)
            car_two.fd(cartworand)
            
            if car_one.xcor() >= 600: #car
                wrt = turtle.Turtle()
                wrt_sc = turtle.Screen()
                wrt_sc.tracer(2)
                wrt.speed(9)
                wrt.ht()
                wrt.penup()
                wrt.color("White")
                wrt.goto(0, -275)
                wrt.pendown()
                wrt.write("The car won! Don't worry though, we're all winners!",
                          True, "center", font =
                    ("Verdana", 18, "normal"))
                
            if car_two.xcor() >= 600: #bus
                wrt = turtle.Turtle()
                wrt_sc = turtle.Screen()
                wrt_sc.tracer(2)
                wrt.speed(9)
                wrt.ht()
                wrt.penup()
                wrt.color("White")
                wrt.goto(0, -275)
                wrt.pendown()
                wrt.write("The bus won! Don't worry though, we're all winners.",
                          True, "center", font =
                    ("Verdana", 18, "normal"))
                
main()

#Thank you to Vishal Chandra, Paul Connoly and Nolan Roberts for helping me with
# some coding issues.