from flask import Flask, request, render_template, redirect, url_for
import logging
import os

app = Flask(__name__)

# Logging to file
logging.basicConfig(filename='server.log', level=logging.INFO)

ADMIN_PASSWORD = 'sup3r_s3cr3t_p4ss'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Log ALL login attempts insecurely
        logging.info(f"Login attempt: username={username}, password={password}")

        if username == 'admin' and password == ADMIN_PASSWORD:
            return render_template('home.html', flag="CTF{l0gg3d_4nd_l34k3d}")
        else:
            return render_template('index.html', error="Invalid credentials")
    return render_template('index.html')


@app.route('/logs')
def show_logs():
    with open('server.log') as f:
        return f"<pre>{f.read()}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
