from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname="postgres"
        )
        return "Connected to DB!"
    except:
        return "DB not ready"

app.run(host="0.0.0.0", port=5000)