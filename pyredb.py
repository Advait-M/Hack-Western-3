#!/usr/bin/env python3

from pyrebase import *

class WaitNoMore:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyCp7LZ2OzFE8odO1WAtPx7f2gLIsCJSc8g",
            "authDomain": "https://wait-no-more.firebaseapp.com",
            "databaseURL": "https://wait-no-more.firebaseio.com",
            "storageBucket": "wait-no-more.appspot.com"
            }

        self.firebase = initialize_app(self.config)

        self.db = self.firebase.database()


    def start(self):
        self.stream = self.db.stream(self.streamHandler)
        self.addSession("Jeffy", "Guffy", "2:00", "4:00", "Waterloo", "Medicare")
        self.addSession("Ert", "Geh", "4:00", "9:00", "Yeth", "Medicare")
        self.addSession("Bob", "Hiw", "1:00", "7:00", "Toronto", "Health Plus")
        #self.editSession("Nim", "Feteov", "15:00", "18:00", "Toronto", "med")
        #self.getAll()
        # times = {"Start Time" : "01:00", "End Time" : "03:00"}
        # self.db.child("Bob Fred").set(times)
        ##endTime = {"End Time": "8:00"}
        ##self.db.child("Bob Fred").set(endTime)
        
    def addSession(self, firstName, lastName, startTime, endTime, location, clinicName):
        self.db.child(firstName + " " + lastName).set({"Start Time" : startTime, "End Time" : endTime, "Location" : location, "Clinic Name" : clinicName})

    def editSession(self, startTime, endTime, name, location, clinicName):
        if typeOfString == "Start Time" or typeOfString == "End Time":
            self.db.child(oldFirstName + " " + oldLastName).update({typeOfString : newString})

    def getAll(self):
        # print((self.db.child("wait-no-more").get()).each())
        # print(type(self.db))
        # print((self.db.child("/").get()).each())
        # for i in range(0, len(self.db)):
        all_users = self.db.child("/").get()
        masterList = []
        for user in all_users.each():
            name = user.key()
            startTime = (user.val())["Start Time"]
            endTime = (user.val())["End Time"]
            location = (user.val())["Location"]
            clinicName = (user.val())["Clinic Name"]
            masterList.append([startTime, endTime, name, location, clinicName])
        print(masterList)
        return masterList

    def streamHandler(self, post):
        event = post["event"]
        key = post["path"]
        value = post["data"]

        if event == "put":
            print(key, ":", value)

if __name__ == "__main__":
    WaitNoMore().start()
    WaitNoMore().getAll()
