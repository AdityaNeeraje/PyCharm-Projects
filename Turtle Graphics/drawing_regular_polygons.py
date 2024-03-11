from turtle import Screen, Turtle
from math import sin, pi, cos
from tkinter import TclError, messagebox
from time import sleep

root = Screen()
turtle = Turtle()
turtle.pensize(5)
turtle.hideturtle()
continue_running = True
try:
    while continue_running:
        while True:
            n = root.numinput(title="Create your own Polygons", prompt="How many sides would you like in your polygon?",
                              default=5, minval=3)
            if n is None:
                continue_running = not messagebox.askyesno(message="Are you sure you want to exit this program?", default="no")
                if not continue_running:
                    root.bye()
                    break
            else:
                n = int(n)
                break

        # # Method 1 - This method creates the polygon anticlockwise, as well as using angles rather than coordinates.
        # turtle.clear()
        # turtle.penup()
        # turtle.goto(x=-50/sin(pi/n), y=0)
        # turtle.setheading(180)
        # turtle.right(90 - 180/n)
        # turtle.pendown()
        # for move in range(n):
        #     turtle.right(360/n)
        #     turtle.forward(100)

        # Method 2 - This method creates the polygon clockwise, and uses coordinates rather than angles.
        turtle.clear()
        turtle.penup()
        turtle.goto(x=50 / sin(pi / n), y=0)
        turtle.pendown()
        for move in range(1, n + 1):
            turtle.goto(x=50 * cos(2 * pi * move / n) / sin(pi / n), y=50 * sin(2 * pi * move / n) / sin(pi / n))

        # The following lines of code check for either a messagebox press or clicking Enter to continue, Esc to escape
        # # Method 1
        def exit_loop():
            global continue_running, root, wait_for_permission
            wait_for_permission = False
            continue_running = False
            root.bye()


        def continue_loop():
            global continue_running, wait_for_permission
            wait_for_permission = False
            continue_running = True


        wait_for_permission = True
        turtle.penup()
        if root.canvheight > 50 / sin(pi / n):
            turtle.goto(0, root.canvheight)
        else:
            turtle.goto(0, root.canvheight/2)
        turtle.color("red")
        turtle.write("Press Enter to Continue, Escape to Exit.", font=("Verdana", 16, "bold"), align="center")
        turtle.color("black")
        while wait_for_permission:
            turtle.goto(0,0)
            root.listen()
            sleep(0.1)
            root.onkey(exit_loop, "Escape")
            root.onkey(continue_loop, "Return")

        # TODO Check how to continue the program if the messagebox is closed without a proper value. If not, make the Method 1 code better.
        # should_continue = messagebox.askyesno(title="Hope you had a nice time drawing Polygons",
        #                                       message="Would you like to continue?", default="yes")
        # print(should_continue)
        # if should_continue:
        #     continue_running = True
        # elif not should_continue:
        #     continue_running = False
        # else:
        #     confirm_exit = messagebox.askyesno(message="Are you sure you want to exit this program?", default="no")
        #     if not confirm_exit:
        #         continue_running = True
        #     else:
        #         continue_running = False
    root.bye()
    root.mainloop()
except (KeyboardInterrupt, TclError) as error:
    pass
