from flask import Flask, render_template
import datetime 
import random
import pyredb
app = Flask(__name__)
now = datetime.datetime.now()


def hexadecimalf():
    hexadecimal = "#"
    sumi = 0
    for i in range(0, 6):
        a = random.randint(48, 70)
        while 58 <= a <= 64:
            a = random.randint(48,70)
        hexadecimal += chr(a)
        sumi += a
    if sumi < 700:
        return hexadecimal
    else:
        return hexadecimalf()

# @app.route("/")
# def index():
data = pyredb.WaitNoMore().getAll()
#     names = []
#     print(data)
#     clinicNames= []
#     for obj1 in range(len(data)):
#         clinicInfo = {
#             'clinic_name' : data[obj1][4],
#             'end_time' : data[obj1][1],
#             'location' : data[obj1][3],
#             'start_time': data[obj1][0],
#             'cooLatitude':  geolocator.geocode(data[obj1][3]).latitude,
#             'cooLongitutde': geolocator.geocode(data[obj1][3]).longitude
#         }
#         clinicNames.append(data[obj1][4])
#         names.append(clinicInfo);
#
#     clinicNames = list(set(clinicNames))
#     print(clinicNames)
#     clinicNames = {}
#     return render_template("index.html", names = names)

# def waitTime(currentTime):
#     SessionEnds =
#     for i in range(len(data)):
#         print(currentTime, currentTime-datetime)
    
if __name__ == "__main__":
    print(data)
    pyredb.WaitNoMore().start()
    app.run()



