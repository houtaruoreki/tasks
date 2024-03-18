# Flask Diary Application

This Flask application is a simple diary management system where users can register, log in, add, edit, and delete diary
entries.

## Setup Instructions

1. **Clone the Repository:**
- git clone https://github.com/houtaruoreki/tasks/tree/test/console%20app/_flask

2. **Install Dependencies:**
- cd flask-diary-app
- pip install -r requirements.txt
3. **Database Setup:**
- This application uses SQLite as its database. You need to initialize the database before running the application.
- Run the following commands to set up the database:
  ```
  sqlite3 diarybook.db < schema.sql
  ```
4. **Run the Application:**
- python3 app.py

The application will run locally on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Functionality

- **Registration:** Users can register by providing a username and password.
- **Login:** Registered users can log in to access the diary functionalities.
- **Logout:** Users can log out of their accounts.
- **Add Diary Entry:** Logged-in users can add diary entries with a memo and optional tags.
- **Edit Diary Entry:** Users can edit existing diary entries.
- **Delete Diary Entry:** Users can delete their diary entries.
- **View Diary Entries:** Upon login, users can view their diary entries.

## API Endpoints

- **GET `/`**: Homepage. If not logged in, redirects to the login page. Displays diary entries for logged-in users.
- **GET `/login`**: Login page. Users can log in here.
- **POST `/login`**: Handles user login.
- **GET `/register`**: Registration page. New users can register here.
- **POST `/register`**: Handles user registration.
- **GET `/logout`**: Logs out the current user.
- **POST `/add_diary`**: Adds a new diary entry.
- **DELETE `/delete_diary`**: Deletes a diary entry.
- **PUT `/edit_diary`**: Edits an existing diary entry.

## Miscellaneous

- The application uses a simple SQLite database named `diarybook.db`.
- The Flask application is structured following the Model-View-Controller (MVC) pattern.
- Passwords are stored in plain text in this example. In a real-world scenario, passwords should be securely hashed.

## Dependencies

- **Flask**: Micro web framework for Python.
- **SQLite3**: Lightweight disk-based database.
- **Jinja2**: Template engine for Python.
- **Werkzeug**: WSGI utility library for Python.

## Note

- This application is intended for educational purposes and may not be suitable for production environments without further enhancements, especially regarding security.


