from tkinter import *
from tkinter import Tk, Entry, END
# name , start time , end time, id
apptO = []


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
        ind =elementFind(st)
        minutes = int(apptO[ind][1][apptO[ind][1].find(":")+1:])
        hour = int(apptO[ind][1][:apptO[ind][1].find(":")])
        minutes /= 60
        return hour + minutes

    def add_appt(self, startTime, endTime, name, location):
        bu = Button(text=name, font="Times 10", relief="groove", bg="lightblue",command=lambda: edit(name))
        apptO.append([name, startTime, endTime, bu])
        y1 = 50 * (calender.start(self, name) - 7) + 10
        y2 = 50 * (calender.start(self, name) - 7) + 10
        x1 = 5
        x2 = 200

        windowID = self.ID.create_window(x1, y1, window=bu, anchor=W, width=x2 - x1, height=50)


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

def elementFind(name,i=0):
    temp = [item[i] for item in apptO]
    if name in temp:
        return temp.index(name)

def edit(name):
    global editFrame
    global clickedFirst, firstName, clickedLast, lastName
    editFrame.destroy()
    editFrame = Frame(editMainFrame)
    editFrame.pack()
    ind = elementFind(name)
    Startminutes = apptO[ind][1][apptO[ind][1].find(":")+1:].zfill(2)
    Starthour = apptO[ind][1][:apptO[ind][1].find(":")]

    Endminutes = apptO[ind][2][apptO[ind][2].find(":")+1:].zfill(2)
    Endhour = apptO[ind][2][:apptO[ind][2].find(":")].zfill(2)

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
    Button(editFrame, text="submit", command=lambda: submitEdit(firstName, lastName, vsth, vstm, vEh, vEm, ind)).pack()


def formatTime(time):
    timesList = time.split(":")
    hours = timesList[0].zfill(2)
    minutes = timesList[1].zfill(2)
    formattedTime = hours + ":" + minutes
    return formattedTime


def submitEdit(firstName, lastName, stH, stM, etH, etM, ind):
    fn = firstName.get()
    ln = lastName.get()
    startTime = stH.get() + ":" + stM.get()
    endTime = etH.get() + ":" + etM.get()
    apptO[ind] = [startTime, endTime, fn+" "+ln]
    fullUpdate()


def fullUpdate():
    global c
    c.ID.delete(ALL)
    for i in apptO:
        startTime, endTime, name = i[0], i[1], i[2]


    c.add_appt(startTime, endTime, name, "None")

root = Tk()
window = PanedWindow(root, height=650, width=800, orient=HORIZONTAL)
window.pack(fill=BOTH, expand=1)

calenderFrame = Frame(window)
calenderFrame.pack()
window.add(calenderFrame)

editMainFrame = Frame(window)
editMainFrame.pack(side=RIGHT)
window.add(editMainFrame)

editFrame = Frame(editMainFrame)

c = calender(calenderFrame)
c.make_grid()
c.add_appt("9:00", "9:30", "Leon Fattakhov", "superCool")
# c.add_appt("10:00", "11:00", "Advait Fattakhov", "superCool")
# c.add_appt("12:30", "12:45", "Nim Fattakhov", "superCool")

root.mainloop()
