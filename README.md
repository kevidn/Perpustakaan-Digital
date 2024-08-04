# Digital Library

This repository contains a Digital Library web application built with Django. The application features CRUD operations, user authentication (Register & Login), and user access levels (UAL) with different permissions for borrowers, staff, and administrators.

## Features

- **CRUD Operations**: Manage books and loans efficiently.
- **User Authentication**: Secure registration and login for users.
- **User Access Levels**:
  - **Peminjam**: Can browse and borrow books.
  - **Petugas**: Can add, edit, and delete book and loan data.
  - **Administrator**: Can register borrowers and manage book and loan data.

## Getting Started

1. Clone the repository
   ```sh
   git clone https://github.com/kevidn/Perpustakaan-Digital.git
   ```
2. Navigate to the project directory
   ```sh
   cd Perpustakaan-Digital
   ```
3. Install the dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the environment variables
   ```sh
   cp .env.example .env
   ```
5. Run the database migrations
   ```sh
   python manage.py migrate
   ```
6. Create a superuser for admin access
   ```sh
   python manage.py createsuperuser
   ```
7. Run the development server
   ```sh
   python manage.py runserver
   ```
