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
        
    def addSession(self, startTime, endTime, name, location, clinicName):
        self.db.child(name).set({"Start Time" : startTime, "End Time" : endTime, "Location" : location, "Clinic Name" : clinicName})

    def editSession(self, startTime, endTime, oldname, name, location, clinicName):
        self.db.child(oldname).remove()
        self.db.child(name).set({"Start Time": startTime, "End Time": endTime, "Location": location, "Clinic Name": clinicName})


    def getAll(self):
        all_users = self.db.child("/").get()
        masterList = []
        for user in all_users.each():
            name = user.key()
            startTime = (user.val())["Start Time"]
            endTime = (user.val())["End Time"]
            location = (user.val())["Location"]
            clinicName = (user.val())["Clinic Name"]
            masterList.append([startTime, endTime, name, location, clinicName])
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
