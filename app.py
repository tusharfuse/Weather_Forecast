from flask import Flask , render_template , request
import requests
app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template("index.html")

@app.route('/weatherapp',methods = ['POST'])
def get_weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {'q':request.form.get("city"), # put id in quotation
              'appid':request.form.get("appid"),
              'units':request.form.get("units")
              }
    
    response = requests.get(url,params= param)
    data = response.json()
    data['city']
    return f"data : {data} , city :{city}"


if __name__ == "__main__":
    app.run(debug = True)