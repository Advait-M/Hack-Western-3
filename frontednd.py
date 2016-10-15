from tkinter import *

import math


class calender():
    def __init__(self, master):
        self.ID = Canvas(master, height=200, width=1000)
        self.ID.pack()

    def make_grid(self):
        x = 10
        y = 20
        y2 = 200
        for i in range(7, 19):
            self.ID.create_text(x, 0, text=i, anchor=N)
            self.ID.create_line(x, y, x, y2)
            x += 85

    def start(self, st):
        minutes = int(st[(st.find(":") + 1):])
        hour = int(st[:st.find(":")])
        minutes /= 60
        return hour + minutes

    def add_appt(self, startTime, endTime, name, description):
        x1 = 90 * (calender.start(self, startTime) - 7) + 10
        x2 = 90 * (calender.start(self, endTime) - 7) + 10
        y = 60
        y2 = 140
        a = (x2 - x1) / 8
        # if a < 5:
        #     name=""
        self.bu = Button(text=name, font="Times 10", height=4, width=int(a), relief="groove", bg="lightblue",
                         command=edit)
        windowID = self.ID.create_window((x1 + x2) / 2, 100, window=self.bu)
        # self.ID.create_rectangle(x1, y, x2, y2, fill="blue")

        # self.ID.create_text((x1+x2)/2, 100, text=name)


def edit():
    Label(editFrame, text="Name").pack()
    Name = Entry(editFrame)
    Name.pack()
    Hours = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    Label(editFrame, text="Time").pack()
    Time = Frame(editFrame)
    vsth = IntVar()
    optStH = OptionMenu(Time, vsth, *Hours)
    vsth.set(7)
    optStH.pack(side=LEFT)
    Label(Time,text=":").pack(side=LEFT)
    vstm = IntVar()
    optStM = OptionMenu(Time, vstm, *[str(i) for i in range(00, 60,5)])
    vstm.set(15)
    optStM.pack(side=LEFT)
    Time.pack()


    Label(editFrame, text="Time End").pack()
    Time2 = Frame(editFrame)
    vEh = IntVar()
    optStH = OptionMenu(Time2, vEh, *Hours)
    vsth.set(7)
    optStH.pack(side=LEFT)
    Label(Time2,text=":").pack(side=LEFT)
    vEm = IntVar()
    optEM = OptionMenu(Time2, vEm, *[str(i) for i in range(00, 60,5)])
    vstm.set(15)
    optEM.pack(side=LEFT)
    Time2.pack()


root = Tk()
window = PanedWindow(root, height=650, width=1000, orient=VERTICAL)
window.pack(fill=BOTH, expand=1)

calenderFrame = Frame(window)
calenderFrame.pack()
window.add(calenderFrame)

editFrame = Frame(window)
editFrame.pack()
window.add(editFrame)

c = calender(calenderFrame)
c.make_grid()
c.add_appt("9:30", "10:10", "Leon \nFattakhov", "superCool")
c.add_appt("10:15", "11:50", "Advait \nFattakhov", "superCool")
c.add_appt("12:30", "12:45", "Nim \nFattakhov", "superCool")
root.mainloop()
