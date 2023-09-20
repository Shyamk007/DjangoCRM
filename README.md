# DjangoCRM
Django CRM, short for "Customer Relationship Manager," is a web-based application built using the Django framework, Python, HTML, CSS, Bootstrap, and MySQL. This project serves as a simple yet effective tool for managing customer data and relationships within your organization. It includes a user-friendly administrative panel where authenticated admins can perform Create, Read, Update, and Delete (CRUD) operations on customer records.

# Features
User Authentication: Utilizes Django's built-in authentication system to secure access to the application. Admins can log in using their username and password.
Admin Dashboard: Provides an intuitive dashboard for authenticated admin users, where they can manage customer data effortlessly.
Customer Data Management: Allows admins to perform CRUD operations on customer records, making it easy to add, view, update, and delete customer information.
Data Validation: Implements data validation and form handling to ensure the integrity of customer data.
Database Backend: Utilizes MySQL as the database backend to store customer information securely.

# Technology Used
Django: A high-level Python web framework that simplifies web development tasks.
HTML: Used for structuring the web pages and rendering content.
CSS: Enhances the presentation and styling of the web application.
Bootstrap: Provides a responsive and aesthetically pleasing user interface.
MySQL: A robust and reliable relational database management system for storing and managing customer data.

# Getting Started 
1. Clone this repository to your local machine
```git clone https://github.com/your-username/django-crm.git```
2.Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
3.Set up your MySQL database and update the database configurations in settings.py.
4.Apply database migrations:
```python manage.py migrate```
5.Create a superuser for admin access:
```python manage.py createsuperuser```
6.Start the development server:
```python manage.py runserver```
7.Access the admin panel at http://localhost:8000/admin/ and log in using the superuser credentials.
8.You're ready to start managing your customer data!
