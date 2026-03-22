from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    # Running on port 3001 to avoid conflict with App_1
    app.run(host='0.0.0.0', port=3001)
