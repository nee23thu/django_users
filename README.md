# User Management API

## Overview
This is a Django-based User Management API that provides CRUD operations for managing user data.

## Features
- Create, Read, Update, and Delete (CRUD) users.
- Uses Django REST framework

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- PostgreSQL (or SQLite for local development)
- Git

### Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/nee23thu/django_users.git
   cd user_management
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Pre-Installation Steps**
Install Django and required frameworks:
   ```sh
   pip install django djangorestframework psycopg2-binary
   ```
4. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

5. **Configure the Database**
   - Modify `settings.py` to configure PostgreSQL or use SQLite.
   - Apply migrations:
     ```sh
     python manage.py migrate
     ```

6. **Run the Server**
   ```sh
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Users
| Method | Endpoint                 | Description                |
|--------|--------------------------|----------------------------|
| GET    | `/api/users`             | List all users |
| POST   | `/api/users`             | Create a new user |
| GET    | `/api/users/{id}`        | Get a user by ID |
| PUT    | `/api/users/{id}`        | Update user details |
| PATCH  | `/api/users/{id}`        | Partially update user details |
| DELETE | `/api/users/{id}`        | Delete a user |

## Example Usage
- Create a new user:
  ```sh
  curl -X POST "http://127.0.0.1:8000/api/users" -H "Content-Type: application/json" \
       -d '{"first_name": "James", "last_name": "Aurthur", "email": "james.aurthur@gmail.com"}'
  ```
## Framework Commands

### Create a new Django project:
```sh
django-admin startproject user_management
```

### Create a new Django app:
```sh
python manage.py startapp users
```

### Apply database migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

### Run Django development server:
```sh
python manage.py runserver
```
## Contributing
Contributions are welcome! Fork the repo, create a new branch, make your changes, and submit a pull request.
