# 🎉 Event Registration Web App

A simple full-stack web application that allows users to register for events. Built using **Flask (Python)**, **HTML**, and **MySQL**, this project demonstrates basic form handling and database integration.

---

## 📌 Features

- 📝 Event registration form  
- 💾 Stores user data in MySQL  
- ⚙️ Backend powered by Flask  
- 🔗 Frontend + Backend + Database integration  

---

## 🛠️ Tech Stack

- **Frontend:** HTML  
- **Backend:** Flask (Python)  
- **Database:** MySQL  

---

## 📂 Project Structure
---

## 🌐 How It Works

1. User opens the homepage  
2. Enters name and event  
3. Submits the form  
4. Flask processes the request  
5. Data is stored in MySQL  
6. Success message is displayed  

---

## 🧾 Database Setup

Run the following SQL commands:

```sql
CREATE DATABASE college;

USE college;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    event VARCHAR(100)
);
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )
pip install flask mysql-connector-python
python app.py
http://127.0.0.1:5000/

---
contributors
Niyati Parekh
Khushi Prajapati
