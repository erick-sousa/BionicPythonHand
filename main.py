#pyfirmata imports
from pyfirmata import SERVO
import pyfirmata
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d
import math

import classtest

#tkinter import and setup
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Hand Controller")

#pyfirmata setup
board = pyfirmata.Arduino('com3')

fingers = []
pins =['11', '10', '9', '6', '5']
x=0
for pin in pins:
    fingers.append(classtest.Assignment_Functions(180, board, pins[x]))
    board.digital[int(pin)].mode = SERVO
    x+=1

angles1 = classtest.UI_Creation()
angles1.creatui(root, fingers)

for finger in fingers:
    finger.boardname.write(180)

my_string_var = tk.StringVar(value="")
def angledata():
    invalids = (angles1.getinput(fingers))

    if len(invalids) == 0:
        my_string_var.set("Angles Set")
    else:
        my_string_var.set("Finger(s) " + ', '.join(invalids) + " contain invalid inputs, enter a value 0-180")

    plot()


#Button
submit = Button(root, text="Submit Angles", width=11, command=angledata).grid(row=3, column=2)

#Spacer
spacerlabel = Label(root, textvariable=my_string_var).grid(row=4, column=0, columnspan=5)

#Spacer
spacerlabel23 = Label(root, text=" ").grid(row=9, column=2)

#Spacer
spacerlabel4 = Label(root, text=" ").grid(row=12, column=2)


def plot():
    def map(x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    plt.close()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Draw a circle on the x=0 'wall'
    p = Rectangle((2, 0), 8, 9, alpha=.9)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_zlim(0, 10)

    colors = ['red', 'blue', 'green', 'pink', 'orange']

    def math_plot(baseangle, midangle, tipangle, x):
        yii1 = 3 * math.cos(baseangle) + 9
        zii1 = 3 * math.sin(baseangle)

        yii2 = 3 * math.cos(midangle) + yii1
        zii2 = 3 * math.sin(midangle) + zii1

        yii3 = 2 * math.cos(tipangle) + yii2
        zii3 = 2 * math.sin(tipangle) + zii2

        if x == 4:
            xi1, yi1, zi1 = [10, yii1, yii2, yii3], [4.5, 4.5, 4.5, 4.5], [0, zii1, zii2, zii3]
        else:
            xi1, yi1, zi1 = [9.96 - 2.62*x, 9.96 - 2.62*x, 9.96 - 2.62*x, 9.96 - 2.62*x], [9, yii1, yii2, yii3], [0, zii1, zii2, zii3]

        ax.plot3D(xi1, yi1, zi1, colors[x])
    x=0
    for finger in fingers:
        if finger.degrees < 45:
            baseangle = map(finger.degrees, 44, 0, 0, 70)
            midangle = math.radians(90 + baseangle)
            tipangle = math.radians(70 + (85 + baseangle))
            baseangle = math.radians(baseangle)
            math_plot(baseangle, midangle, tipangle, x)
        elif 104 > finger.degrees > 44:
            baseangle = 0
            midangle = map(finger.degrees, 120, 45, 0, 85)
            tipangle = math.radians(85 + midangle)
            midangle = math.radians(midangle)
            math_plot(baseangle, midangle, tipangle, x)
        else:
            baseangle = 0
            midangle = 0
            tipangle = map(finger.degrees, 180, 119, 0, 60)
            tipangle = math.radians(tipangle)
            math_plot(baseangle, midangle, tipangle, x)
        x+=1

    plt.show(block=False)

root.mainloop()

