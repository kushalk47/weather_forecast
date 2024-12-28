from flask import Flask , render_template
import pandas as pd

app=Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filename=r"csv 2/TG_STAID"+str(station).zfill(6)+".txt"
    df =pd.read_csv(r"filename",skiprows=20,)
    temperature =10
    return {station:"station",date:"date",temperature:"23"}


if __name__=="__main__":
    app.run(debug=True)