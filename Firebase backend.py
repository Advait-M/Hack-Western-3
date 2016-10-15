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
        self.addSession("Jeffy", "Guffy", "2:00", "4:00")
        #self.editSession()
        self.getAll()
        # times = {"Start Time" : "01:00", "End Time" : "03:00"}
        # self.db.child("Bob Fred").set(times)
        ##endTime = {"End Time": "8:00"}
        ##self.db.child("Bob Fred").set(endTime)
        
    def addSession(self, firstName, lastName, startTime, endTime):
        self.db.child(firstName + " " + lastName).set({"Start Time" : startTime, "End Time" : endTime})

    def editSession(self, oldFirstName, oldLastName, newString, typeOfString):
        if typeOfString == "Start Time" or typeOfString == "End Time":
            self.db.child(oldFirstName + " " + oldLastName).update({typeOfString : newString})

    def getAll(self):
        all_users = db.child("wait-no-more").get()
        for user in all_users.each():
            print(user.key())  # Morty
            print(user.val())  # {name": "Mortimer 'Morty' Smith"}

    def streamHandler(self, post):
        event = post["event"]
        key = post["path"]
        value = post["data"]

        if event == "put":
            print(key, ":", value)

WaitNoMore().start()

print("a")
