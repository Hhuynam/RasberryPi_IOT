import time
import random  # Thêm import random
from flask import Flask, render_template
from pyrebase import pyrebase

app = Flask(__name__)

# Cài đặt Firebase
config = {
    "apiKey": "AIzaSyB2w0FZFA5WcRVphAYVTwhHRnXqhxdn4HM",
    "authDomain": "hahuynam16122024.firebaseapp.com",
    "databaseURL": "https://hahuynam16122024-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "hahuynam16122024",
    "storageBucket": "hahuynam16122024.firebasestorage.app",
    "messagingSenderId": "903576852556",
    "appId": "1:903576852556:web:3c69e837dd06df737cfce9",
    "measurementId": "G-J4WC3Y9BTX"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route('/')
def home():
    return render_template('index.html')

def update_temperature():
    while True:
        # Sử dụng random để giả lập dữ liệu nhiệt độ
        temperature = random.uniform(15.0, 30.0)
        data = {
            "temperature": temperature,
            "timestamp": time.time()
        }
        db.child("temperatures").push(data)
        time.sleep(5)  # Cập nhật mỗi 5 giây

if __name__ == '__main__':
    from threading import Thread
    t = Thread(target=update_temperature)
    t.start()
    app.run(debug=True, use_reloader=False)
