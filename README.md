# -------------------------- Teacher-Portal --------------------------


------------- Credentials ----------------.
Teacher:-
	Username: teacher
	Password: teacher@123

Admin:-
	Username: teacher
	Password: teacher@123
	
# 🛠️ Django Project Setup Guide

Welcome to this Teacher Portal django project! This guide will walk you through setting up and running the project on your local machine using a virtual environment (`.venv`).
---

## ✅ Prerequisites

Make sure the following tools are installed:

- ✅ Python 3.10+ → [Download Python](https://www.python.org/downloads/)
- ✅ Git → [Download Git](https://git-scm.com/)
- ✅ Code Editor (VS Code - Optional)
- ✅ Internet connection

---

## 🚀 Setup Instructions

### 🔧 Step 1: Install Python

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest version for your OS.
3. **During installation**, check the box:
   ```
   ✅ Add Python to PATH
   ```
4. Open a terminal and verify the installation:

   ```bash
   python --version
   ```

   Expected output:
   ```
   Python 3.10 (or higher)
   ```

---

### 📁 Step 2: Get the Project Files

#### Option 1: Clone using Git

```bash
git clone https://github.com/your-username/your-django-project.git
cd your-django-project
```

#### Option 2: Download ZIP

1. Download the project as a ZIP from GitHub.
2. Extract it and open the folder in terminal.

---

### 🧪 Step 3: Create and Activate Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

You’ll know it’s activated when you see `(.venv)` at the beginning of your terminal line.

---

### 📦 Step 4: Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

If you get an error that `requirements.txt` is missing, run:

```bash
pip freeze > requirements.txt
```

> ⚠️ Always activate `.venv` before installing packages.

---

### 🔄 Step 5: Apply Migrations

Set up your database tables:

```bash
python manage.py migrate
```

---

### 👤 Step 6 (Optional): Create a Superuser

Create an admin user for the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

---

### 🌐 Step 7: Run the Development Server

Start your Django app:

```bash
python manage.py runserver
python manage.py runserver 0.0.0.0:80
```

Then open your browser at:

```
http://127.0.0.1:8000/  | http://localhost:8000
http://127.0.0.1        | http://localhost
```

If the server is running correctly, you’ll see the Django welcome page or your custom homepage.

---

## 📑 Common Django Commands

| Purpose                  | Command                            |
| ------------------------ | ---------------------------------- |
| Activate venv (Windows)  | `.venv\Scripts\activate`           |
| Activate venv (macOS/Linux) | `source .venv/bin/activate`    |
| Install requirements     | `pip install -r requirements.txt`  |
| Create migrations        | `python manage.py makemigrations`  |
| Apply migrations         | `python manage.py migrate`         |
| Create superuser         | `python manage.py createsuperuser` |
| Run server               | `python manage.py runserver`       |
| Open admin panel         | `http://127.0.0.1:8000/admin/`     |

---


## 🙌 Final Notes

- 💡 Always activate your virtual environment before development.
- ⌨️ Use `CTRL+C` to stop the development server.
- 🔁 Don’t forget to commit your changes often if using Git!

---
