# Mini-Project-DBMS

## 🐾 Project Title

**Pet Adoption Management System (PAMS)**

---

## 🎯 Project Overview

A web-based application that helps users browse adoptable pets, submit adoption requests, and manage adoption records. The admin can add, update, and remove pets and view adoption applications. The data is stored in a relational database and can be exported for reporting.

---

## 💡 Key Objectives

1. Implement CRUD operations using a relational DBMS.
2. Demonstrate normalization and relationships between entities (pets, users, adoptions, etc.).
3. Use SQL queries for data retrieval and manipulation.
4. Provide a web interface for interaction with the database.
5. Enable data export (e.g., CSV, Excel, or PDF).

---

## 🧱 System Architecture

**3-tier architecture:**

1. **Frontend (Presentation Layer)** — web UI for users and admin
2. **Backend (Application Layer)** — handles logic, routes, and DB operations
3. **Database Layer** — stores all data related to pets, users, and adoption requests

---

## ⚙️ Tools and Technologies

| Component | Recommended Tools / Frameworks |
| --- | --- |
| **Frontend** | HTML, CSS, JavaScript, Bootstrap (for layout) |
| **Backend** | Flask (Python) or Node.js (Express) |
| **Database** | MySQL / PostgreSQL / SQLite (for simplicity) |
| **ORM (optional)** | SQLAlchemy (for Flask) |
| **Exporting Data** | Pandas (Python) or CSVWriter (Node.js) |
| **Testing & Local Server** | XAMPP (for MySQL + PHP), or Flask’s built-in dev server |
| **Version Control** | Git + GitHub |
| **Deployment (optional)** | Render / Railway / Heroku (for hosting) |

---

## 🧩 Database Design

### Entities

1. **Users**
    - user_id (PK)
    - name
    - email
    - phone
    - address
2. **Pets**
    - pet_id (PK)
    - name
    - species (Dog, Cat, Rabbit, etc.)
    - breed
    - age
    - gender
    - status (Available / Adopted)
3. **Adoption_Requests**
    - request_id (PK)
    - user_id (FK → Users)
    - pet_id (FK → Pets)
    - request_date
    - status (Pending / Approved / Rejected)
4. **Admin** *(optional)*
    - admin_id (PK)
    - username
    - password

---

## 🧠 Functional Modules

### 👤 User Side

- Register / login
- View available pets (with filters like species, age, etc.)
- Submit adoption request form
- View status of adoption request

### 🐶 Admin Side

- Add new pets to database
- Update pet details or mark adopted
- View all adoption requests and approve/reject them
- Export adoption data (CSV or Excel)

---

## 🖥️ Implementation Steps

| Phase | Description | Tools |
| --- | --- | --- |
| **1. Requirement Analysis** | Define functionalities, user roles, and data flow | — |
| **2. Database Design** | Design ER diagram and normalize tables | MySQL Workbench / Draw.io |
| **3. Backend Setup** | Build REST APIs for CRUD operations | Flask or Node.js |
| **4. Frontend Design** | Create HTML templates and connect forms | HTML/CSS/JS |
| **5. Database Integration** | Connect to MySQL/PostgreSQL | SQLAlchemy / MySQL connector |
| **6. Export Feature** | Add button to download data | CSV or Excel export library |
| **7. Testing & Deployment** | Test CRUD and adoption workflow | localhost or cloud host |

---

---

- Image upload for pets (store file paths in DB)
- Search and filter system
- Email notification on request approval
- Admin analytics dashboard (adoption trends)

---

## 🧮 Expected Learning Outcomes

- Understanding of relational schema design
- CRUD operations using SQL
- Backend-frontend integration
- Data export and reporting
- Basic web development workflow
