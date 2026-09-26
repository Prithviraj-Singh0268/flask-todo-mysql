import os
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task
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

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Medium")

        if not title:
            flash("Title is required.", "danger")
            return redirect(url_for("add_task"))

        task = Task(title=title, description=description, priority=priority)
        db.session.add(task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_task.html")

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            flash("Title is required.", "danger")
            return redirect(url_for("edit_task", task_id=task.id))

        task.title = title
        task.description = request.form.get("description", "").strip()
        task.priority = request.form.get("priority", "Medium")
        db.session.commit()
        flash("Task updated successfully!", "success")
        return redirect(url_for("index"))

    return render_template("edit_task.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)