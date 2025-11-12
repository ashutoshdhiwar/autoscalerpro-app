from flask import Flask, render_template, redirect, url_for
import platform, socket, datetime, psutil, os

app = Flask(__name__)

start_time = datetime.datetime.now()

@app.route('/')
def home():
    uptime = datetime.datetime.now() - start_time
    return render_template(
        'index.html',
        server_name=socket.gethostname(),
        system=platform.system(),
        release=platform.release(),
        arch=platform.architecture()[0],
        cpu=psutil.cpu_percent(interval=1),
        memory=psutil.virtual_memory().percent,
        uptime=str(uptime).split('.')[0],
        current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/health')
def health():
    return {"health": "ok", "status": 200}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
