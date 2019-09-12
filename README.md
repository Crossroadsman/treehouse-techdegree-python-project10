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
- [x] Create Todo. When the save link is clicked, handle the request by:
  - [x] Creating a route that:
  - [x] Creates a Todo, and
  - [x] Sets the proper status code
  - [x] `POST /api/v1/todos` creates a new Todo, returns it, and sets the appropriate status code
- [x] Update Todo. When a previously saved Todo is updated and the save link is clicked, handle the request by:
  - [x] Creating a route that:
  - [x] Updates the existing Todo record
  - [x] `PUT /api/v1/todos/xxx` is handled and the proper Todo is updated
- [x] Delete Todo. When a previously saved Todo is deleted and the save link is clicked, handle the request by:
  - [x] Creating a route that:
  - [x] Deletes the record
  - [x] Returns a blank response
  - [x] Returns the proper status code
  - [x] `DELETE /api/v1/todos/xxx` deletes the appropriate Todo, sends back the appropriate status code and an empty body
- [x] Unit Testing. Write unit tests to ensure:
  - [x] Each view displays the correct information
  - [x] Models behave as expected
  - [x] Classes behave as expected
  - [x] Other functions behave as expected
  - [x] Coverage is at least 50%
- [x] Code is clean, readable, well-organized, PEP8 compliant

### Extra Credit Features ###

- [x] Increase test coverage to >= 75%

