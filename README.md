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

Feature Checklist
-----------------

### Base Features ###

- [ ] API is versioned
  - [ ] all routes should be prefixed with `/api/v1`
- [ ] Fetch all Todos
  - [ ] Handle the request
  - [ ] Create appropriate route
  - [ ] Return all the Todos
- [ ] Create Todo. When the save link is clicked, handle the request by:
  - [ ] Creating a route that:
  - [ ] Creates a Todo, and
  - [ ] Sets the proper status code
- [ ] Update Todo. When a previously saved Todo is updated and the save link is clicked, handle the request by:
  - [ ] Creating a route that:
  - [ ] Updates the existing Todo record
- [ ] Delete Todo. When a previously saved Todo is deleted and the save link is clicked, handle the request by:
  - [ ] Creating a route that:
  - [ ] Deletes the record
  - [ ] Returns a blank response
  - [ ] Returns the proper status code
- [ ] Unit Testing. Write unit tests to ensure:
  - [ ] Each view displays the correct information
  - [ ] Models behave as expected
  - [ ] Classes behave as expected
  - [ ] Other functions behave as expected

### Extra Credit Features ###

- [x] Increase test coverage to >= 75%

