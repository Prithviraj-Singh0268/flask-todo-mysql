import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return "Todo App - MySQL connected!"


if __name__ == "__main__":
    app.run(debug=True)