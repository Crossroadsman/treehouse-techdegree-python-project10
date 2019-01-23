Project 10: Todo API with Flask
===============================

Installation
------------
1. Clone the project 
2. Create and activate a venv
3. Install dependencies (listed in requirements.txt)

Usage
-----
Run the application from the `todo` directory:
```console
(venv) $ python3 app.py
```

Run tests from the `todo` directory (unittest should auto discover them):
```console
(venv) $ coverage run -m unittest
```

And get coverage report:
```console
(venv) $ coverage report
```

Project Status
--------------
### Project Instructions ###
- [x] This API is versioned, all routes should be prefixed with `/api/v1`
- [x] When the app first starts it will attempt to fetch all Todos in the 
  system. Handle the request and return all the Todos.
- [ ] When a Todo is created and the save link is clicked, it will make a 
  request to the server. Handle request by:
  - [ ] creating a Todo; and
  - [ ] setting the proper status code
- [ ] When a previously saved Todo is updated and the save link is clicked, it
  will make a request to the server. Handle the request by updating the 
  existing Todo.
- [ ] When a previously saved Todo is deleted and the save link is clicked, it
  will make a request to the server.
  - [ ] handle the deletion;
  - [ ] return a blank response;
  - [ ] return the proper status code.
- [ ] Unit test the app:
  - [ ] >50% test coverage;
  - [ ] >75% test coverage.
  
### How You Will Be Graded ###
- [ ] Peewee Model Classes for adding/editing/deleting Todo entries
- [ ] Fetching Todos
  - [ ] `GET /api/v1/todos` returns all todos; and
  - [ ] populates web application.
- [ ] Create a new Todo
  - [ ] `POST /api/v1/todos` creates a new Todo;
  - [ ] returns it; and
  - [ ] sets the appropriate status code.
- [ ] Update an existing Todo
  - [ ] `PUT /api/v1/todos/xxx` is handled; and
  - [ ] proper Todo is updated.
- [ ] Delete an existing Todo
  - [ ] `DELETE /api/v1/todos/xxx` deletes the appropriate Todo;
  - [ ] sends back the appropriate status code; and
  - [ ] an empty body.
- [ ] Unit test the app
  - [ ] There are unit tests for all the views;
  - [ ] models; and
  - [ ] other functions.
  - [x] Test coverage >=50%
  - [x] Test coverage >75%
- [x] Python Code Style
  - [x] Code is clean, readable, and well organized;
  - [x] Complies with most common PEP8 standards.
  
