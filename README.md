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
12345678901234567890123456789012345678901234567890123456789012345678901234567890
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
