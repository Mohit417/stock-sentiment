from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route("/")
def index():
   return render_template("insert_company.html")

@app.route("/company.html", methods = ["GET"])
def classify():
    cName = request.form['companyName']
    return render_template("company.html",name = cName)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


