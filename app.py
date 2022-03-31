from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/temperature")
def temperature():
    from requests_html import HTMLSession
    s= HTMLSession()

    url = 'https://www.google.com/search?q=weather+satara&rlz=1C1CHBD_enIN930IN930&oq=weathersatara&aqs=chrome.1.69i57j0i10l6.7158j1j7&sourceid=chrome&ie=UTF-8'

    r = s.get(url)

    #temperature and unit
    temp = r.html.find("span#wob_tm", first=True).text
    unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
    # print(temp,unit)

    #humidity
    humidity = r.html.find("span#wob_hm", first=True).text
    # print(humidity)

    #infoabout how was the day
    desc = r.html.find("div.VQF4g", first=True).find("span#wob_dc", first=True).text
    # print(desc)

    #perception
    perception = r.html.find("span#wob_pp", first=True).text
    # print(perception)

    #wind flow rate
    wind = r.html.find("span#wob_ws", first=True).text
    # print(wind)    

    return render_template('Temperature.html',variable1=temp,variable2=unit,variable3=humidity,variable4=desc,variable5=perception,variable6=wind)

@app.route("/AirQualityIndex")
def AirQualityIndex():
    #Air Quality index
    from requests_html import HTMLSession

    s= HTMLSession()

    url = 'https://www.accuweather.com/en/in/satara/189287/air-quality-index/189287'

    r = s.get(url)

    #air_pollution
    Air_polution = r.html.find("div.aq-number-container", first=True).find("div.aq-number", first=True).text
    Air_polution_unit = r.html.find("div.aq-number-container", first=True).find("div.aq-unit", first=True).text
    # print(Air_polution, Air_polution_unit)


    #pollutants
    PM10 = r.html.find("div.air-quality-pollutant", first=True).find("h3.column", first=True).text
    # print("Partculate Matter :", PM10)

    pollutant_index = r.html.find("div.column.mobile-middle", first=True).find("div.pollutant-index", first=True).text
    pollutant_concent = r.html.find("div.column.mobile-middle", first=True).find("div.pollutant-concentration", first=True).text
    # print(pollutant_index)
    # print(pollutant_concent)

    return render_template('AirQualityIndex.html',variable7=Air_polution,variable8=Air_polution_unit,variable9=PM10,variable10=pollutant_index,variable12=pollutant_concent)

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
