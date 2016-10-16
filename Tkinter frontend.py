from time import strftime
from tkinter import *
from tkinter import Tk, Entry, END
from tkinter.filedialog import asksaveasfile
import pyredb

# start time , end time, name , location, clinic name
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

    def start(self, st, row):
        ind = elementFind(st)
        minutes = int(apptO[ind][row][apptO[ind][row].find(":") + 1:])
        hour = int(apptO[ind][row][:apptO[ind][row].find(":")])
        minutes /= 60
        return hour + minutes

    def add_appt(self, startTime, endTime, name, locationNAME, clinicName):
        bu = Button(text=name, relief="groove", font="Times 14",bg="lightblue",command=lambda: edit(name, True))
        apptO.append([startTime, endTime, name, locationNAME, clinicName])
        y1 = 50 * (calender.start(self, name, 0) - 7) + 20
        y2 = 50 * (calender.start(self, name, 1) - 7) + 20
        x1 = 5
        x2 = 200
        pyredb.WaitNoMore().addSession(startTime, endTime, name, locationNAME, clinicName)
        windowID = self.ID.create_window(x1, y1, window=bu, anchor=NW, width=x2 - x1, height=y2 - y1)

        # def currentWith(self):


def check():
    global clinicName, locationNAME
    file = open("start.txt", 'r+')
    clinicName = file.readline()
    locationNAME = file.readline()

    if len(locationNAME) > 0 and len(clinicName) > 0:
        clinicName = clinicName

    else:
        from tkinter import Tk, Entry, Label, Button, W

        def send():
            global clinicName
            clinic = lEntry.get()
            locationNAME = cEntry.get()
            clinicName = clinic
            if locationNAME == " " or clinic == " ":
                pass
            else:
                file.write(clinic + '\n' + locationNAME)
                popupWindow.destroy()
                file.close()

        def KeyDownHandler(event):
            send()

        popupWindow = Tk()
        Label(popupWindow, text="Clinic Name").grid(row=1, column=1, sticky=W)
        cEntry = Entry(popupWindow , font="Times 16")
        cEntry.grid(row=2, column=2, sticky=W)
        Label(popupWindow, text="Address").grid(row=2, column=1, sticky=W)
        lEntry = Entry(popupWindow, font="Times 16")
        lEntry.grid(row=1, column=2, sticky=W)
        Button(popupWindow, text="Submit",font="Times 16", command=send).grid(row=3, column=1, sticky=W)

        popupWindow.bind("<Return>", KeyDownHandler)
        popupWindow.wm_protocol("WM_DELETE_WINDOW", lambda: None)
        popupWindow.mainloop()


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


def elementFind(name, i=2):
    temp = [item[i] for item in apptO]
    if name in temp:
        return temp.index(name)


def edit(name, real):
    global editFrame, clickedFirst, firstName, clickedLast, lastName
    editFrame.destroy()
    editFrame = Frame(editMainFrame)
    editFrame.pack()
    ind = elementFind(name)
    Startminutes = apptO[ind][0][apptO[ind][0].find(":") + 1:].zfill(2)
    Starthour = apptO[ind][0][:apptO[ind][0].find(":")]

    Endminutes = apptO[ind][1][apptO[ind][1].find(":") + 1:].zfill(2)
    Endhour = apptO[ind][1][:apptO[ind][1].find(":")].zfill(2)
    if real:
        name = apptO[ind][2].split(" ")
    print(name)

    Label(editFrame, text="Name").pack()
    firstName = Entry(editFrame, font="Times 16", fg="grey", exportselection=0)
    clickedFirst = False
    firstName.bind("<FocusIn>", callbackFirst)
    if not real:
        firstName.insert(0, "First Name")
    else:
        firstName.insert(0, name[0])
    firstName.pack()
    lastName = Entry(editFrame, font="Times 16", fg="grey", exportselection=0)
    clickedLast = False
    lastName.bind("<FocusIn>", callbackLast)
    if not real:
        lastName.insert(0, "Last Name")
    else:
        lastName.insert(0, name[1])  # "Last Name")
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
    Button(editFrame, text="Submit",font="Times 16", command=lambda: submitEdit(firstName, lastName, vsth, vstm, vEh, vEm, ind)).pack()


def formatTime(time):
    timesList = time.split(":")
    hours = timesList[0].zfill(2)
    minutes = timesList[1].zfill(2)
    formattedTime = hours + ":" + minutes
    return formattedTime


def submitEdit(firstName, lastName, stH, stM, etH, etM, ind):
    global clinicName, locationNAME
    fn = firstName.get()
    ln = lastName.get()
    startTime = stH.get() + ":" + stM.get()
    endTime = etH.get() + ":" + etM.get()
    apptO[ind] = [startTime, endTime, fn + " " + ln, apptO[ind][3], locationNAME, clinicName]
    editFrame.destroy()
    g.config(state="normal")
    print(apptO)
    fullUpdate()


def pullDB():
    global apptO
    apptO = pyredb.WaitNoMore().getAll()
    fullUpdate()

def fullUpdate():
    global c
    c.ID.delete(ALL)
    c.make_grid()
    for i in range(len(apptO) - 1, -1, -1):
        startTime, endTime, name, address, cName = apptO[i][0], apptO[i][1], apptO[i][2], apptO[i][3], apptO[i][4]
        c.add_appt(startTime, endTime, name, address, cName)
        # for j  in range(len(apptO)-1, -1, -1):
        del apptO[i]


def add():
    apptO.append(["07:00", "08:00", "First Name Last Name", locationNAME,
                  clinicName])  # appends defaults for editing thus creating a new session
    edit("First Name Last Name", False)
    g.config(state="disabled")


check()

root = Tk()
root.title(clinicName)
window = PanedWindow(root, height=650, width=800, orient=HORIZONTAL)
window.pack(fill=BOTH, expand=1)

calenderFrame = Frame(window)
calenderFrame.pack()
window.add(calenderFrame)

editMainFrame = Frame(window)
editMainFrame.pack(side=RIGHT)
window.add(editMainFrame)
editFrame = Frame(editMainFrame)
editFrame.pack(side=BOTTOM)

def saveNotes():
    f = asksaveasfile(mode='w+', defaultextension=".txt",filetypes=[('Note', '.txt')])
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(notes.get(1.0, END))  # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()





g = Button(editMainFrame, text="\u271A Add Patient", font="Times 16", command=add)
g.pack(side=TOP, fill=BOTH)
def reDraw():
    global notes
    notes= Text(editMainFrame, height=10)
    Button(editMainFrame, text="Save Note", command=saveNotes).pack(side=BOTTOM)
    notes.pack(side=BOTTOM, fill=X)
    Label(editMainFrame, text="Notes", font = "Times 16").pack(side=BOTTOM)

reDraw()


c = calender(calenderFrame)
c.make_grid()

# c.add_appt("9:00", "10:00", "Leon Fattakhov", "234 King Street East Waterloo On", "WingWong Clinc of Kong")
# c.add_appt("10:00", "11:00", "Advait Fattakhov", "390 Cavendish Dr Waterloo On", "Clinic Of Death")
# c.add_appt("12:30", "12:45", "Nim Fattakhov", "235 King Street East Waterloo On", "KingKong Clinc of Wong")
pullDB()
root.mainloop()
