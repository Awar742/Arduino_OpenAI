from bottle import route, run, request, template

latest_data = {"temperature": None, "humidity": None}

@route('/')
def home():
    return template("""
        <h1>Дані з Arduino</h1>
        <p>Температура: {{temp}} °C</p>
        <p>Вологість: {{hum}} %</p>
    """, temp=latest_data["temperature"], hum=latest_data["humidity"])

@route('/update', method='POST')
def update():
    try:
        data = request.json
        latest_data["temperature"] = data.get("temperature")
        latest_data["humidity"] = data.get("humidity")
        return {"status": "ok"}
    except:
        return {"status": "error", "message": "Невірний формат"}

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, debug=True)
