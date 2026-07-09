<div align="center">

# ✅ MyTodo

### *A clean, no-nonsense to-do list app — built with Flask, styled with Bootstrap.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 What is this?

**MyTodo** is a full-stack, CRUD-powered task manager. It's small on purpose — no bloat, no over-engineering — just a Flask backend talking to a SQLite database, rendering clean Jinja templates styled with Bootstrap 5.

Add a task. Update it. Delete it. That's the whole deal — done well.

## ✨ Features

- 📝 **Create** — add a todo with a title and description
- 🔄 **Update** — edit any existing todo in place
- 🗑️ **Delete** — remove todos you no longer need
- 🕒 **Auto-timestamped** — every todo remembers when it was created
- 💅 **Responsive UI** — Bootstrap 5 navbar and layout, works on mobile too
- 🪶 **Lightweight** — SQLite database, zero external services required

## 🛠️ Tech Stack

| Layer          | Technology                          |
|----------------|--------------------------------------|
| Backend        | Flask 3.1, Flask-SQLAlchemy 3.1     |
| Database       | SQLite                              |
| Frontend       | Jinja2 templates + Bootstrap 5.3    |
| Deployment     | Gunicorn (Procfile included)         |

## 📂 Project Structure

```
mytodo/
├── app.py                 # Flask app, routes, and the Todo model
├── requirements.txt        # Python dependencies
├── templates/
│   ├── base.html           # Shared layout (navbar, Bootstrap includes)
│   ├── index.html          # Home page — add + view todos
│   └── update.html         # Edit an existing todo
└── static/                 # (optional) images, custom CSS, JS go here
```

## 🚀 Getting Started

### 1. Clone the repo

```bash
https://github.com/prathmesh0work/Flask-My-Todo.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

The database (`todo.db`) is created automatically on first run. Open your browser at:

```
http://127.0.0.1:5000
```

## ☁️ Deployment

This repo ships with a `Procfile`, so it's ready to deploy on any platform that supports Gunicorn (Render, Railway, Heroku, etc.):

```
web: gunicorn app:app
```

Just point your platform of choice at this repo, make sure `requirements.txt` is installed, and it'll boot straight up.

## 🗺️ Roadmap

- [ ] Mark todos as complete / incomplete
- [ ] Due dates + priority levels
- [ ] Search and filter todos
- [ ] User authentication (multi-user support)
- [ ] Dark mode 🌙

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](../../issues) or open a PR.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Prathmesh**
🔗 [GitHub](https://github.com/prathmesh0work)

---

<div align="center">
  <sub>Built with ☕, Flask, and a healthy dislike of unfinished tasks.</sub>
</div>
