# TodoApp

A full-stack task management web application built with Flask and MySQL, developed as a learning project to practice backend web development.

## Features
- Add, edit, and delete tasks
- Mark tasks as complete with a single click
- Set task priority (Low / Medium / High)
- Persistent storage using MySQL (via SQLAlchemy ORM)
- Flash messages for user feedback
- Clean, responsive UI built with Bootstrap 5

## Tech Stack
- Python 3
- Flask
- Flask-SQLAlchemy
- MySQL
- HTML / CSS (Bootstrap)

## Project Structure
TodoApp/
├── app.py # Flask routes and app entry point
├── models.py # SQLAlchemy Task model
├── requirements.txt
├── .env.example # Template for required environment variables
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── add_task.html
│ └── edit_task.html
└── static/
└── style.css

## Setup
```bash
git clone https://github.com/Prithviraj-Singh0268/flask-todo-mysql.git
cd flask-todo-mysql
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

Create a MySQL database and a `.env` file based on `.env.example`:
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=todo_db
SECRET_KEY=change-this-in-production


Run the app:
```bash
python app.py
```

Visit `http://127.0.0.1:5000`. Tables are created automatically on first run.

## Possible Future Improvements
- User authentication (multiple users, private task lists)
- Due dates and reminders
- REST API endpoints
- Search and filter by priority/status
- Unit tests with pytest

## Status
✅ Core CRUD features complete