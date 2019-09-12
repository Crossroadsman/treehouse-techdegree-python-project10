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

### Application ###

Run the application from the `todo` directory:
```console
(venv) $ python3 app.py
```

**Important Usage Note**: When creating a Todo item, clicking anywhere on the page outside the text entry area is recognised
by the Angular application as ending the text entry action and returning to the list view. Accordingly, clicking 'save' 
during the text entry process **_is not recognised as a save request by the Angular App_** but merely as an 'end of text 
entry' action. The save link is not recognised by the Angular app until the text editing action has ended.

### Testing ###

Run tests from the `todo` directory (unittest should auto discover them):
```console
(venv) $ coverage run -m unittest
```

And view the coverage report:
```console
(venv) $ coverage report
```

Or generate a detailed HTML report from the coverage results:
```console
(venv) $ coverage html
```


Feature Checklist
-----------------

### Base Features ###

- [x] API is versioned
  - [x] all routes should be prefixed with `/api/v1`
- [x] Fetch all Todos
  - [x] Handle the request
  - [x] Create appropriate route
  - [x] Return all the Todos
  - [x] `GET /api/v1/todos` returns all Todos and populates the web application
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

