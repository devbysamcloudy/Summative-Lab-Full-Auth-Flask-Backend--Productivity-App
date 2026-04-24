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
cd Summative-Lab-Full-Auth-Flask-Backend--Productivity-App
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

---

## Authentication Flow

1. Register an account via `POST /signup`
2. Log in via `POST /login` — you will receive a JWT `access_token`
3. Copy the token and include it in all protected requests:

```
Authorization: Bearer <your_token>
```

---

## API Endpoints

### Auth Routes

---

**Register**

```
POST /signup
```

Request body:

```json
{
  "username": "sammy",
  "email": "sammy@example.com",
  "password": "yourpassword"
}
```

Success response `201`:

```json
{
  "message": "User created successfully"
}
```

Error response `400` (username taken):

```json
{
  "error": "Username already exists"
}
```

---

**Login**

```
POST /login
```

Request body:

```json
{
  "username": "sammy",
  "password": "yourpassword"
}
```

Success response `200`:

```json
{
  "access_token": "<jwt_token>"
}
```

Error response `401`:

```json
{
  "error": "Invalid credentials"
}
```

---

**Get current user** *(protected)*

```
GET /me
```

Headers:

```
Authorization: Bearer <your_token>
```

Success response `200`:

```json
{
  "username": "sammy"
}
```

Error response `404`:

```json
{
  "error": "User not found"
}
```

---

### Notes Routes *(all protected)*

All note routes require the following header:

```
Authorization: Bearer <your_token>
```

---

**Create a note**

```
POST /notes
```

Request body:

```json
{
  "title": "My Note",
  "content": "This is my note"
}
```

Success response `201`:

```json
{
  "message": "Note created successfully",
  "note_id": 1
}
```

---

**Get all notes** *(paginated)*

```
GET /notes?page=1&per_page=5
```

Query params:

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| page | int | 1 | Page number |
| per_page | int | 5 | Results per page |

Success response `200`:

```json
{
  "note": [
    {
      "id": 1,
      "title": "My Note",
      "content": "This is my note"
    },
    {
      "id": 2,
      "title": "Another Note",
      "content": "More content here"
    }
  ]
}
```

---

**Update a note**

```
PATCH /notes/<id>
```

Request body (all fields optional):

```json
{
  "title": "Updated title",
  "content": "Updated content"
}
```

Success response `200`:

```json
{
  "message": "Note updated successfully"
}
```

Error response `404`:

```json
{
  "error": "Note not found"
}
```

---

**Delete a note**

```
DELETE /notes/<id>
```

Success response `200`:

```json
{
  "message": "Note deleted successfully"
}
```

Error response `404`:

```json
{
  "error": "Note not found"
}
```

---

## Testing with Postman

1. Set `Content-Type: application/json` on all requests
2. Hit `POST /signup` to create an account
3. Hit `POST /login` and copy the `access_token` from the response
4. For all protected routes, go to the **Authorization** tab in Postman, select **Bearer Token**, and paste the token

---

## Security

- Passwords hashed with bcrypt
- JWT required on all note routes
- Users can only access their own notes
- Proper HTTP error codes returned for unauthorized access

---

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

---

## Author

Backend developed as part of Flask Summative Lab – Productivity API Project

- GitHub: [devbysamcloudy](https://github.com/devbysamcloudy/Summative-Lab-Flask-SQLAlchemy-Workout-Application-Backend)
- Email: snganga685@gmail.com
