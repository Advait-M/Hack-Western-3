from tkinter import *
from tkinter import Tk, Entry, END

import math


class calender():
    def __init__(self, master):
        self.ID = Canvas(master, height=700, width=250)
        self.ID.pack()

    def make_grid(self):
        x = 10
        y = 20
        x2 = 200
        for i in range(7, 19):
            self.ID.create_text(210, y, text=i)
            self.ID.create_line(x, y, x2, y)
            y += 50

    def start(self, st):
        minutes = int(st[(st.find(":") + 1):])
        hour = int(st[:st.find(":")])
        minutes /= 60
        return hour + minutes

    def add_appt(self, startTime, endTime, name, description):
        self.ST = startTime
        self.ET = endTime
        self.name = name
        y1 = 50 * (calender.start(self, startTime) - 7) + 10
        y2 = 50 * (calender.start(self, endTime) - 7) + 10
        x1 = 5
        x2 = 200

        self.bu = Button(text=name, font="Times 10", relief="groove", bg="lightblue",
                         command=lambda: edit(c))
        windowID = self.ID.create_window(x1, y1, window=self.bu, anchor=W, width=x2 - x1, height=50)


def callbackFirst(event):
    global clickedFirst, firstName
    if (clickedFirst == False):
        firstName.delete(0, END)
        firstName.config(fg="black")
        clickedFirst = True


def callbackLast(event):
    global clickedLast, lastName
    if (clickedLast == False):
        lastName.delete(0, END)
        lastName.config(fg="black")
        clickedLast = True


def edit(calenderOBJ):
    global clickedFirst, firstName, clickedLast, lastName
    Startminutes = int(calenderOBJ.ST[(calenderOBJ.ST.find(":") + 1):])
    Starthour = int(calenderOBJ.ST[:calenderOBJ.ST.find(":")])

    Endminutes = int(calenderOBJ.ET[(calenderOBJ.ET.find(":") + 1):])
    Endhour = int(calenderOBJ.ET[:calenderOBJ.ET.find(":")])

    Label(editFrame, text="Name").pack()
    firstName = Entry(editFrame, fg="grey", exportselection=0)
    clickedFirst = False
    firstName.bind("<FocusIn>", callbackFirst)
    firstName.insert(0, "First Name")
    firstName.pack()
    lastName = Entry(editFrame, fg="grey", exportselection=0)
    clickedLast = False
    lastName.bind("<FocusIn>", callbackLast)

    lastName.insert(0, "Last Name")
    lastName.pack()
    allHours = [str(item).zfill(2) for item in list(range(7, 19))]
    allMinutes = [str(item).zfill(2) for item in list(range(0, 60, 5))]
    Label(editFrame, text="Time").pack()
    Time = Frame(editFrame)
    vsth = StringVar()
    optStH = OptionMenu(Time, vsth, *allHours)
    vsth.set(Starthour)

    optStH.pack(side=LEFT)
    Label(Time, text=":").pack(side=LEFT)
    vstm = StringVar()
    optStM = OptionMenu(Time, vstm, *allMinutes)
    vstm.set(Startminutes)
    optStM.pack(side=LEFT)
    Time.pack()

    Label(editFrame, text="Time End").pack()
    Time2 = Frame(editFrame)
    vEh = StringVar()
    optStH = OptionMenu(Time2, vEh, *allHours)
    vEh.set(Endhour)
    optStH.pack(side=LEFT)
    Label(Time2, text=":").pack(side=LEFT)
    vEm = StringVar()
    optEM = OptionMenu(Time2, vEm, *allMinutes)
    vEm.set(Endminutes)
    optEM.pack(side=LEFT)
    Time2.pack()
    Button(editFrame, text="submit", command=lambda: submitEdit(firstName, lastName, vsth, vstm, vEh, vEm)).pack()


def formatTime(time):
    timesList = time.split(":")
    hours = timesList[0].zfill(2)
    minutes = timesList[1].zfill(2)
    formattedTime = hours + ":" + minutes
    return formattedTime


def submitEdit(firstName, lastName, stH, stM, etH, etM):
    fn = firstName.get()
    ln = lastName.get()
    startTime = stH.get() + ":" + stM.get()
    endTime = etH.get() + ":" + etM.get()
    print(fn, ln, startTime, endTime)


root = Tk()
window = PanedWindow(root, height=650, width=800, orient=HORIZONTAL)
window.pack(fill=BOTH, expand=1)

calenderFrame = Frame(window)
calenderFrame.pack()
window.add(calenderFrame)

editFrame = Frame(window)
editFrame.pack(side=RIGHT)
window.add(editFrame)

c = calender(calenderFrame)
c.make_grid()
c.add_appt("9:00", "9:30", "Leon Fattakhov", "superCool")
c.add_appt("10:00", "11:00", "Advait Fattakhov", "superCool")
c.add_appt("12:30", "12:45", "Nim Fattakhov", "superCool")
root.mainloop()
