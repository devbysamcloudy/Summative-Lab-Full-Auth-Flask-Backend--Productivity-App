# Flask Notes API

A secure REST API for a productivity application with JWT authentication.

## Description

This backend allows users to sign up and log in securely using JWT authentication, create and manage personal notes, and access only their own data. Pagination is supported when retrieving notes.

## Technologies

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-Bcrypt
- SQLite

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/devbysamcloudy/Summative-Lab-Full-Auth-Flask-Backend--Productivity-App
cd <your-project-folder>
```

**2. Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:

```
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
```

**5. Set up the database**

```bash
flask db upgrade
```

**6. Seed the database (optional)**

```bash
python seed.py
```

## Running the App

```bash
python3 run.py
```

Server runs at `http://127.0.0.1:5000`

## Authentication Flow

1. Create an account via `POST /signup`
2. Log in via `POST /login` to receive a JWT token
3. Include the token in all protected requests:

```
Authorization: Bearer <your_token>
```

## API Endpoints

### Auth Routes

**Register**

```
POST /signup
```

```json
{
  "username": "sammy",
  "email": "sammy@example.com",
  "password": "yourpassword"
}
```

**Login**

```
POST /login
```

```json
{
  "username": "sammy",
  "password": "yourpassword"
}
```

**Get current user** *(protected)*

```
GET /me
```

---

### Notes Routes *(all protected)*

**Create a note**

```
POST /notes
```

```json
{
  "title": "My Note",
  "content": "This is my note"
}
```

**Get all notes** *(paginated)*

```
GET /notes?page=1&per_page=5
```

**Get a single note**

```
GET /notes/<id>
```

**Update a note**

```
PATCH /notes/<id>
```

```json
{
  "title": "Updated title",
  "content": "Updated content"
}
```

**Delete a note**

```
DELETE /notes/<id>
```

---

## Security

- Passwords hashed with bcrypt
- JWT required on all note routes
- Users can only access their own notes
- Proper HTTP error codes returned for unauthorized access

## Testing with Postman

- Set `Content-Type: application/json` on all requests
- For protected routes, add the Authorization header:

```
Authorization: Bearer <token>
```

## Project Structure

```
app/
  models/
    user.py
    note.py
  routes/
    auth_routes.py
    note_routes.py
  schemas/
    user_schema.py
    note_schema.py
  utilis/
    auth_utilis.py
  config.py
  extensions.py
  __init__.py

seed.py
run.py
Readme.md
```

## Author

Backend developed as part of Flask Summative Lab – Productivity API Project
