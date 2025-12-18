# Backend Dashboard API

This project is a modular backend built as part of a Backend Developer Intern task.  
It demonstrates clean backend architecture, REST API design, authentication, and database integration.

---

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy
- JWT Authentication

---

## Project Structure

backend-dashboard/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│
│ ├── auth/
│ │ └── router.py
│ ├── dashboard/
│ │ └── router.py
│ ├── analytics/
│ │ └── router.py
│ ├── leads/
│ │ └── router.py
│ ├── sales/
│ │ └── router.py
│ ├── content/
│ │ └── router.py
│ ├── settings/
│ │ └── router.py
│
├── requirements.txt
├── README.md


---

## Features
- Modular backend architecture
- JWT-based authentication
- CRUD APIs for all modules
- Database integration using SQLAlchemy
- Clean and scalable folder structure

---

## Modules & APIs

### Authentication
- `POST /auth/register` – Register a new user
- `POST /auth/login` – Login and receive JWT token

### Dashboard
- `POST /dashboard`
- `GET /dashboard`

### Analytics
- `POST /analytics`
- `GET /analytics`

### Leads
- `POST /leads`
- `GET /leads`

### Sales
- `POST /sales`
- `GET /sales`

### Content
- `POST /content`
- `GET /content`

### Settings
- `POST /settings`
- `GET /settings`

---

## Authentication Flow
1. Register using `/auth/register`
2. Login using `/auth/login`
3. Use the returned JWT token in `Authorization: Bearer <token>`
4. Access protected module APIs

---

## Installation

```bash
pip install -r requirements.txt


uvicorn app.main:app --reload
