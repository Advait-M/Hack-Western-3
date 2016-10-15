from flask import Flask, render_template
import pyredb
app = Flask(__name__)

@app.route("/")
def index():
    #Test Case
    return render_template("index.html", firstName = "Nim", lastName = "Person")

if __name__ == "__main__":
    pyredb.WaitNoMore().start()
    data = pyredb.WaitNoMore().getAll()
    print(data)
    app.run()



