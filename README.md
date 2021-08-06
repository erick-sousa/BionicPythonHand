# BionicPythonHand

## Background
This program stems from a project to design and create a functional bionic hand using an Arduino and 5 servo motors. All CAD models were made in Fusion360, and the parts were 3D printed with my Artillery Sidewinder X1. Below is a picture of the CAD model I created.

![Image of Bionic Hand CAD Model](https://github.com/erick-sousa/BionicPythonHand/blob/main/pictures/Hand%20CAD.PNG)

## This Repository 
After fully manufacturing the hand and making it work through the Arduino IDE, I hoped to further explore its capabilities by creating a program that would allow me to control the hand through Python. This opened the door to a lot of more creative functionalities for the hand. The code found in this repository is one of my first attempts at working with objects in Python, so there are some inefficiencies, redundancies, and organizational issues that need to be worked out, but overall the code works. The function of the code is to create a TKinter GUI which allows the bionic hand to be controlled. It also has the capability to make a 3D plot of the rough locations of the finger's positions using Matplotlib. A picture of these can be seen below

![Image of TKinter GUI](https://github.com/erick-sousa/BionicPythonHand/blob/main/pictures/Tkinter%20GUI.png)
![Image of Matplotlib Graph](https://github.com/erick-sousa/BionicPythonHand/blob/main/pictures/Matplotlib%20Graph.png)

In the [classes](classes.py) file you will find the Classes that I developed to do a few tasks. 
- UI_Creation handles creating the majority of the TKinter elements used in the UI
- Assignment_Functions initializes the object by creating object instances for each finger in the hand which is referenced by Class_UI in creating the buttons. This class also holds most of the commands used by the TKinter GUI

The two classes work together to make the GUI work properly. The organization of the classes can be improved as a way to make the program more clarity. 

In the [main](main.py) file, the classes are ran and some other remaining elements from the TKinter GUI are also created. Some elements, such as the Submit Angles button, I felt did not fit in the classes nicely, so it was left in the main file. The other major component of the main.py file is the Matplotlib element which creations a 3D plot of rough finger positions when the Submit Angles button is used.

## Closing
As stated, there are certain flaws that I know about mainly in the organization of the code. As I improve my skills in created classes in Python I hope to fix some of the issues. Besides that, it all functions as intended. In order for the program to function in its current state, it requires the pyfirmata library, information on this library can be found in the [pyfirmata docs](https://pypi.org/project/pyFirmata/). The current setup uses an Arduino UNO on the COM3 port. These can be changed in the main file if you wish.
