Project 10: Todo API with Flask
===============================

Installation
------------
1. Clone the project 
2. Create and activate a venv
3. Install the application dependencies (listed in `requirements.txt`): `pip install -r requirements.txt` from 
   the [`todo`](https://github.com/Crossroadsman/treehouse-techdegree-python-project10/tree/master/todo) directory
4. To test the application, install the testing dependencies (listed in `test-requirements.txt`): 
   `pip install -r test-requirements.txt` from the 
   [`todo`](https://github.com/Crossroadsman/treehouse-techdegree-python-project10/tree/master/todo) directory

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

Feature Checklist
-----------------

### Base Features ###

- [ ] API is versioned
  - [ ] all routes should be prefixed with `/api/v1`
- [ ] Fetch all Todos
  - [ ] Handle the request
  - [ ] Create appropriate route
  - [ ] Return all the Todos
  - [ ] `GET /api/v1/todos` returns all Todos and populates the web application
- [ ] Create Todo. When the save link is clicked, handle the request by:
  - [ ] Creating a route that:
  - [ ] Creates a Todo, and
  - [ ] Sets the proper status code
  - [ ] `POST /api/v1/todos` creates a new Todo, returns it, and sets the appropriate status code
- [ ] Update Todo. When a previously saved Todo is updated and the save link is clicked, handle the request by:
  - [ ] Creating a route that:
  - [ ] Updates the existing Todo record
  - [ ] `PUT /api/v1/todos/xxx` is handled and the proper Todo is updated
- [ ] Delete Todo. When a previously saved Todo is deleted and the save link is clicked, handle the request by:
  - [ ] Creating a route that:
  - [ ] Deletes the record
  - [ ] Returns a blank response
  - [ ] Returns the proper status code
  - [ ] `DELETE /api/v1/todos/xxx` deletes the appropriate Todo, sends back the appropriate status code and an empty body
- [ ] Unit Testing. Write unit tests to ensure:
  - [ ] Each view displays the correct information
  - [ ] Models behave as expected
  - [ ] Classes behave as expected
  - [ ] Other functions behave as expected
  - [ ] Coverage is at least 50%
- [ ] Code is clean, readable, well-organized, PEP8 compliant

### Extra Credit Features ###

- [x] Increase test coverage to >= 75%

