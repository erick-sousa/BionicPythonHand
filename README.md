# BionicPythonHand

## Background
This program stems from a project to design and create a functional bionic hand using an Arduino and 5 servo motors. All CAD models were made in Fusion360, and the parts were 3D printed with my Artillery Sidewinder X1. Below is a picture of the CAD model I created.

![Image of Bionic Hand CAD Model](https://github.com/erick-sousa/BionicPythonHand/blob/main/pictures/Hand%20CAD.PNG)

## This Repository 
After fully manufacturing the hand and making it work through the Arduino IDE, I hoped to further explore it's capabilities by creating a program that would allow me to control the hand through Python. This opened the door to a lot of more creative functionalities for the hand. The code found in this repository is one of my first attempts at working with objects in Python, so there are some inefficiencies, redundancies, and organizational issues that need to worked out, but overall the code works. The function of the code is to create a TKinter GUI which allows the bionic hand to be controlled. It also has the capability to make a 3D plot of the rough locations of the fingers positions using Matplotlib. A picture of these can be seen below

![Image of TKinter GUI](https://github.com/erick-sousa/BionicPythonHand/blob/main/pictures/Tkinter%20GUI.png)
![Image of Matplotlib Graph](https://github.com/erick-sousa/BionicPythonHand/blob/main/pictures/Matplotlib%20Graph.png)

In the [classes](classes.py) you will find the Classes that I developed to do a few tasks. 
-UI_Creation handles creating the majority of the TKinter elements used in the UI
