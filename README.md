# Student-Feedback-Management-System
# 🎓 Student Feedback Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.2-lightgrey)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-00618a)](https://www.mysql.com/)

> A web-based platform for collecting and managing student feedback, enabling institutions to make data-driven decisions and improve educational outcomes.

---

## 📋 Table of Contents
- [🎓 Student Feedback Management System](#-student-feedback-management-system)
  - [📋 Table of Contents](#-table-of-contents)
  - [🌟 Project Description](#-project-description)
  - [🚀 Features](#-features)
  - [🛠️ Setup and Installation](#️-setup-and-installation)
  - [🔄 API Endpoints](#-api-endpoints)
    - [👤 Users API](#-users-api)
    - [❓ Questions API](#-questions-api)
    - [💬 Feedback API](#-feedback-api)
  - [💻 Example Usage](#-example-usage)
  - [🧑 About Me](#-about-me)
  - [🔗 Key Projects](#-key-projects)
  - [📄 License](#-license)

---

## 🌟 Project Description

The **Student Feedback Management System** simplifies the process of collecting and managing student feedback. Designed for educational institutions, the system includes role-based access for students and admins. Students submit feedback on curriculum and campus facilities, while admins analyze this feedback via dashboards to make informed decisions.

---

## 🚀 Features

- **Role-Based Access**:
  - Students: Submit feedback.
  - Admins: View and analyze aggregated feedback.
- **Dynamic Feedback Questions**:
  - Text-based or multiple-choice questions.
- **Real-Time Dashboards** for administrators.
- **Secure Authentication** using Flask-Login.

---

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.8+
- MySQL
- Virtual Environment

### Installation Steps
1. Clone the repository:
```bash
   git clone https://github.com/rhoda-lee/Student-Feedback-Management-System.git
```
2. Move into cloned directory
```bash
   cd Student-Feedback-Management-System
```
3. Create a virtual environment and activate it:
```bash
    sudo apt install python3-venv
    python3 -m venv ~/myenv
    source ~/myenv/bin/activate
```
4. Install dependencies:

```bash
    pip install mysql-connector-python sqlalchemy flask flask-login 
```
5. Set up the database:
```bash
    # Configure the database connection in config/config.py
```
6. Initialize the database:
```bash
    python3 models.py
```
7. Run the Flask application:
```bash
    export FLASK_APP=app
    export FLASK_DEBUG=1
    flask run
```
8. Open your browser and navigate to:

```bash
    http://127.0.0.1:5000
```
## 🔄 API Endpoints
### 👤 Users API

| Endpoint                 | Method | Description               | Example Request                                                                                                                                          | Example Response                                                                                                                                                   |
|--------------------------|--------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/register`              | POST   | Register a new user      | `{ "username": "johndoe", "email": "john@example.com", "password": "password123" }`                                                                       | `{ "message": "Registration successful!" }`                                                                                                                       |
| `/login`                 | POST   | Log in a user            | `{ "email": "john@example.com", "password": "password123" }`                                                                                              | `{ "message": "Welcome back, johndoe!", "redirect": "stu_dash.html" }`                                                                                            |
| `/logout`                | POST   | Log out the current user | -                                                                                                                                                        | `{ "message": "You have been logged out." }`                                                                                                                      |
| `/users`                 | GET    | List all users           | -                                                                                                                                                        | `{ "Users": [{"id": 1, "username": "johndoe", "email": "john@example.com", "role": "user"}] }`                                                                     |
| `/users/<int:user_id>`   | GET    | Get a specific user      | -                                                                                                                                                        | `{ "id": 1, "username": "johndoe", "email": "john@example.com", "role": "user" }`                                                                                  |
| `/users/update/<int:user_id>` | PUT   | Update a user         | `{ "username": "john_updated", "email": "john_updated@example.com", "password": "newpassword123", "role": "user" }`                                       | `{ "message": "User updated successfully." }`                                                                                                                     |
| `/users/delete/<int:user_id>` | DELETE | Delete a user        | -                                                                                                                                                        | `{ "message": "User deleted successfully." }`                                                                                                                     |

### ❓ Questions API

| Endpoint                 | Method | Description               | Example Request                                                                                                                                          | Example Response                                                                                                                                                   |
|--------------------------|--------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/questions`             | POST   | Add a new question       | `{ "question_text": "What is your favorite color?", "question_type": "select", "options": ["Red", "Blue", "Green"] }`                                     | `{ "Message": "Question created successfully!", "Question": { "question_id": 1, "question_text": "What is your favorite color?", "question_type": "select" } }`   |
| `/questions`             | GET    | List all questions       | -                                                                                                                                                        | `{ "Questions": [{"question_id": 1, "question_text": "What is your favorite color?", "question_type": "select", "options": ["Red", "Blue", "Green"]}] }`           |
| `/questions/<int:question_id>` | GET | Get a specific question | -                                                                                                                                                        | `{ "question_id": 1, "question_text": "What is your favorite color?", "question_type": "select", "options": ["Red", "Blue", "Green"] }`                            |
| `/questions/update/<int:question_id>` | PUT | Update a question | `{ "question_text": "What is your favorite fruit?", "question_type": "select", "options": ["Apple", "Banana", "Cherry"] }`                                | `{ "Message": "Question updated successfully." }`                                                                                                                  |
| `/questions/delete/<int:question_id>` | DELETE | Delete a question | -                                                                                                                                                        | `{ "Message": "Question deleted successfully." }`                                                                                                                  |

### 💬 Feedback API

| Endpoint                 | Method | Description               | Example Request                                                                                                                                          | Example Response                                                                                                                                                   |
|--------------------------|--------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/feedback`              | POST   | Create new feedback      | `{ "user_id": 1, "question_id": 2, "response": "I enjoy coding." }`                                                                                       | `{ "Message": "Feedback created successfully!", "Feedback": { "feedback_id": 1, "user_id": 1, "question_id": 2, "response": "I enjoy coding." } }`                |
| `/feedback`              | GET    | List all feedback        | -                                                                                                                                                        | `{ "Feedbacks": [{"feedback_id": 1, "user_id": 1, "question_id": 2, "response": "I enjoy coding."}] }`                                                             |
| `/feedback/<int:feedback_id>` | GET | Get specific feedback   | -                                                                                                                                                        | `{ "feedback_id": 1, "user_id": 1, "question_id": 2, "response": "I enjoy coding." }`                                                                              |
| `/feedback/update/<int:feedback_id>` | PUT | Update feedback       | `{ "response": "I love coding challenges." }`                                                                                                            | `{ "Message": "Feedback updated successfully." }`                                                                                                                  |
| `/feedback/delete/<int:feedback_id>` | DELETE | Delete feedback      | -                                                                                                                                                        | `{ "Message": "Feedback deleted successfully." }`                                                                                                                  |



## 💻 Example Usage
### Testing API Endpoints with Postman
    To test the backend API endpoints using Postman, follow these steps:

#### Users API
1. Register a User
- Endpoint: POST /register
- Request Body:
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "password123"
}
```
- Expected Response:
```json
{
  "message": "Registration successful!"
}
```

2. Login a User
- Endpoint: POST /login
- Request Body:
```json
{
  "email": "johndoe@example.com",
  "password": "password123"
}
```
- Expected Response:
```json
{
  "message": "Welcome back, johndoe!",
  "redirect": "stu_dash.html"
}
```

3. List All Users
- Endpoint: GET /users
- Expected Response:
```json
{
  "Users": [
    {
      "id": 1,
      "username": "johndoe",
      "email": "johndoe@example.com",
      "role": "user"
    }
  ]
}
```

4. Get a Specific User
- Endpoint: GET /users/<int:user_id>
- Example URL: /users/1
- Expected Response:
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "johndoe@example.com",
  "role": "user"
}
```

5. Update a User
- Endpoint: PUT /users/update/<int:user_id>
- Example URL: /users/update/1
- Request Body:
```json
{
  "username": "john_updated",
  "email": "john_updated@example.com",
  "password": "newpassword123",
  "role": "admin"
}
```
- Expected Response:
```json
{
  "message": "User updated successfully."
}
```

6. Delete a User
- Endpoint: DELETE /users/delete/<int:user_id>
- Example URL: /users/delete/1
- Expected Response:
```json
{
  "message": "User deleted successfully."
}
```


#### Questions API
1. Add a New Question
- Endpoint: POST /questions
- Request Body (Text Question):
```json
{
  "question_text": "What are your hobbies?",
  "question_type": "text"
}
```
- Request Body (Select Question):
```json
{
  "question_text": "What is your favorite color?",
  "question_type": "select",
  "options": ["Red", "Blue", "Green"]
}
```
- Expected Response:
```json
{
  "Message": "Question created successfully!",
  "Question": {
    "question_id": 1,
    "question_text": "What is your favorite color?",
    "question_type": "select",
    "options": ["Red", "Blue", "Green"]
  }
}
```

2. List All Questions
- Endpoint: GET /questions
- Expected Response:
```json
{
  "Questions": [
    {
      "question_id": 1,
      "question_text": "What is your favorite color?",
      "question_type": "select",
      "options": ["Red", "Blue", "Green"]
    }
  ]
}
```
3. Get a Specific Question
- Endpoint: GET /questions/<int:question_id>
- Example URL: /questions/1
- Expected Response:
```json
{
  "question_id": 1,
  "question_text": "What is your favorite color?",
  "question_type": "select",
  "options": ["Red", "Blue", "Green"]
}
```

4. Update a Question
- Endpoint: PUT /questions/update/<int:question_id>
- Example URL: /questions/update/1
- Request Body:
```json
{
  "question_text": "What is your favorite fruit?",
  "question_type": "select",
  "options": ["Apple", "Banana", "Cherry"]
}
```
- Expected Response:
```json
{
  "Message": "Question updated successfully."
}
```

5. Delete a Question
- Endpoint: DELETE /questions/delete/<int:question_id>
- Example URL: /questions/delete/1
- Expected Response:
```json
{
  "Message": "Question deleted successfully."
}
```

#### Feedback API
1. Create Feedback
- Endpoint: POST /feedback
- Request Body:
```json
{
  "user_id": 1,
  "question_id": 1,
  "response": "I love learning new things."
}
```
- Expected Response:
```json
{
  "Message": "Feedback created successfully!",
  "Feedback": {
    "feedback_id": 1,
    "user_id": 1,
    "question_id": 1,
    "response": "I love learning new things."
  }
}
```
2. List All Feedback
- Endpoint: GET /feedback
- Expected Response:
```json
{
  "Feedbacks": [
    {
      "feedback_id": 1,
      "user_id": 1,
      "question_id": 1,
      "response": "I love learning new things."
    }
  ]
}
```
3. Get Specific Feedback
- Endpoint: GET /feedback/<int:feedback_id>
- Example URL: /feedback/1
- Expected Response:
```json
{
  "feedback_id": 1,
  "user_id": 1,
  "question_id": 1,
  "response": "I love learning new things."
}
```
4. Update Feedback
- Endpoint: PUT /feedback/update/<int:feedback_id>
- Example URL: /feedback/update/1
- Request Body:
```json
{
  "response": "I enjoy learning Python."
}
```
- Expected Response:
```json
{
  "Message": "Feedback updated successfully."
}
```

5. Delete Feedback
- Endpoint: DELETE /feedback/delete/<int:feedback_id>
- Example URL: /feedback/delete/1
- Expected Response:
```json
{
  "Message": "Feedback deleted successfully."
}
```

### How to Use
- Open Postman.
- Create a new request and set the appropriate method (e.g., POST, GET, PUT, or DELETE).
- Enter the endpoint URL (e.g., http://127.0.0.1:5000/register).
- For endpoints that require data (e.g., POST), go to the Body tab, select raw, choose JSON format, and input the JSON data.
- Click Send and verify the response matches the expected output.








## 🧑 About Me
👋 Hi, I'm Rhoda Lee, a passionate software developer and data science enthusiast. I love creating solutions that solve real-world problems and enjoy contributing to open-source projects.

### 🔍 What I Do:
- Web Development: 
    - Full-stack expertise with Python, Flask, and React.
- Data Science: 
    - Working on projects that analyze and visualize data insights.
Tech Advocacy: 
    - Committed to sharing knowledge and empowering others through workshops and online content.

### 🔗 Key Projects
#### Real Estate Tour Website: A showcase of properties available for rent or sale in Accra.
Data Analysis YouTube Channel: Tutorials and insights into the world of data analysis and visualization.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to fork, contribute, or reach out to collaborate! 😊










