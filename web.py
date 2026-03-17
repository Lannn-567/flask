from flask import Flask,  render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    return "藍浚愷到此一遊"

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = (str(now.day))
    now = year + "/" + month +"/" + day
    return render_template("today.html", datetime = now)

if __name__ == "__main__":
    app.run(debug=True)