from tkinter import *
import functools
class UI_Creation:
    finger_input_list = []

    buttons = []
    buttonNames = ["Contract", "Extend", "Add", "Subtract", "Peace", "Rockstar", "Okay", "Point", "Phone"]     #used for labeling buttons
    buttonRows = [7, 8, 15, 16, 11, 4]      #used for selecting rows of buttons

    labelNames = ["Index", "Middle", "Ring", "Pinky", "Thumb", "Custom Angles", "Quick Moves", "Presets", "Add or Subtract"]
    labelRows = [1, 6, 14, 0, 5, 10, 13]
    labelParams = [None, '#c0c0c2', None, "ridge", 'TkDefaultFont 9 underline']

    def __init__(self):
        pass

    #Method to create the input boxes
    def createinput(self, root, column):
        input = Entry(root, width= 16, borderwidth=1, relief="ridge", justify='center')
        input.grid(row=2, column=column)
        return input

    #Method to create the buttons
    def createbutton(self, root, name, column, row, command):
        button = Button(root, text=name, width=13, command=command)
        button.grid(row=row, column=column)
        return button

    #Method to create the buttons
    def createlabel(self, root, name, color, relief, font, row, column):
        label = Label(root, text=name, width=14, borderwidth=1, bg=color, relief=relief, font=font)
        label.grid(row=row, column=column)


    #Creates all UI elements
    def creatui(self, root, fingers):
        x = 0
        #Adds input boxes to UI
        for finger in fingers:
            associated_inputs = [finger, self.createinput(root, x)]
            self.finger_input_list.append(associated_inputs)
            x+=1

        #Adds buttons to UI
        x, column  = 0, 0
        #Adds Contract/Extend/Add/Sub buttons
        while x <= 3:
            print(fingers)
            for finger in fingers:
                 commands = [finger.contractfinger, finger.extendfinger, finger.addangle, finger.subangle]
                 self.createbutton(root, self.buttonNames[x], column, self.buttonRows[x], functools.partial(commands[x], finger))
                 column += 1
            column = 0
            x+=1

        #Adds preset buttons
        while x<9:
            index = 0
            for finger in fingers:
                otherbuttons = self.createbutton(root, self.buttonNames[x], column, self.buttonRows[4], functools.partial(finger.preset, index, fingers))
                self.buttons.append(otherbuttons)
                column+=1
                x+=1
                index += 1

        x, index, column = 0, 0, 0
        #Adds Labels
        #Index-Thumb labels
        while x <= 2:
            for finger in fingers:
                self.createlabel(root, self.labelNames[index], self.labelParams[1], self.labelParams[3], self.labelParams[0], self.labelRows[x], column)
                index += 1
                column += 1
            index, column = 0, 0
            x+=1
        index = 5

        #Custom Angles/Quick Moves/Presets/AddSub
        while x < 7:
            otherlabels = self.createlabel(root, self.labelNames[index], self.labelParams[0], self.labelParams[0], self.labelParams[4], self.labelRows[x], 2)
            index += 1
            x += 1

    def getinput(self, fingers):
        pin_to_finger = {}
        index=0
        for finger in fingers:
            pin_to_finger[finger.boardname] = self.labelNames[index]
            index += 1

        invalid_fingers = []
        for finger_input in self.finger_input_list:
            if not finger_input[1].get().isnumeric():
                invalid_fingers.append(finger_input[0].boardname)
            elif int(finger_input[1].get()) > 180:
                invalid_fingers.append(finger_input[0].boardname)
            else:
                finger_input[0].degrees = int(finger_input[1].get())
                finger_input[0].boardname.write(finger_input[1].get())

        invalid_fingers_name = []
        for finger in invalid_fingers:
            invalid_fingers_name.append(pin_to_finger[finger])
        return invalid_fingers_name


class Assignment_Functions:
    peace = [180, 180, 0 ,0, 0]
    rock = [180, 0, 0, 180 ,180]
    okay = [0, 180, 180, 180 ,0]
    point = [180, 0, 0, 0, 180]
    phone = [0, 0, 0, 180, 180]
    presets = [peace, rock, okay, point, phone]

    def __init__(self, degrees, board, pin):
        self.degrees = degrees
        self.boardname = board.get_pin('d:'+pin+':o')

    def extendfinger(self, finger):
        self.degrees = 180
        print(self.degrees)
        print("#####################")
        finger.boardname.write(self.degrees)

    def contractfinger(self, finger):
        self.degrees = 0
        print(self.degrees)
        print("#####################")
        finger.boardname.write(self.degrees)

    def anglecheck(self, angle):
        if angle > 180:
            angle = 180
        elif angle < 0:
            angle = 0
        return angle

    def addangle(self, finger):
        self.degrees += 15
        self.degrees = self.anglecheck(self.degrees)
        print(self.degrees)
        print("#####################")
        finger.boardname.write(self.degrees)

    def subangle(self, finger):
        self.degrees -= 15
        self.degrees = self.anglecheck(self.degrees)
        print(self.degrees)
        print("#####################")
        finger.boardname.write(self.degrees)

    def preset(self, index, fingers):
        x=0
        for finger in fingers:
            print(self.presets[index][x])
            finger.degrees = self.presets[index][x]
            finger.boardname.write(self.presets[index][x])
            x+=1
        print("#####################")

    def servowrite(self, index):
        index.write(self.degrees)


# TODO Spacer labels
# TODO possibly implement submit angles to object

