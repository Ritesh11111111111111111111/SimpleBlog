# SimpleBlog

## Introduction

SimpleBlog is a basic blogging platform built using Django and the Django REST framework. It allows users to create (schedule blog posts), read, update, and delete blog posts.

## Features

- User Authentication (Register, Login, Logout).

- CRUD operations for Blog posts.

- Blog Post Scheduling: Users can schedule posts to be published at a specified date and time. 

- Multiple images for each post.

- Pagination: Blogs are delivered in a paginated format.

## Prerequisites

This project requires Django, MySQL, Redis, Django REST_Api and Celery.

## Setup & Installation

1. Clone this repository.
```bash
[git clone https://github.com/Ritesh11111111111111111111/SimpleBlog.git]
```

2. Create a virtual environment and activate it.
```bash
python3 -m venv env
source env/bin/activate
```

3. Install the required packages.
```bash
pip install -r requirements.txt
```

4. Configure your database settings in the `simpleblog/settings.py` file.

5. Run the database migrations.
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Start the redis server on a new terminal
```bash
redis-server
```

7. Start the celery worker on a new terminal
```bash
celery -A simpleblog worker --loglevel=info
```

8. Start the django server
```bash
python3 manage.py runserver
```

Then, you can access the application at `localhost:8000`.

## API Endpoints

- User registration: `POST /register/`
- User login: `POST /login/`
- User logout: `GET /logout/`
- List of all blog posts: `GET /`
- Create a new blog post: `POST /`
- Retrieve an individual blog post: `GET /<int:pk>/`
- Update a blog post: `PUT /<int:pk>/`
- Delete a blog post: `DELETE /<int:pk>/`

## Note
Celery is used to handle the blog post scheduling feature. You need to have a running Redis process and start the celery worker to allow it to execute tasks.

## License
This project is available under the MIT License.

## Contributing
Pull requests are welcome. Please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
