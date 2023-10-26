# Nyasa Care

### Description
<p> Nyasa Care is a multi-user platform where health service providers list their services and allow members of the public to book for their services </p>



### Packages
- Flask
- Flask-SQLAlchemy


### Setup

### Environment variables 
export DATABASE_URI="postgresql://user:pass@host:port/demo_db"


### How to run the app
1. Set the app package (because it has __init__.py) as the place where Flask should look for the create_app() factory function:  ```export FLASK_APP=app ```
2. Set the FLASK_ENV environment variable to run the application in development mode: ```export FLASK_ENV=development ```
3.  Run the application: ``` flask run```

### Folder Structure
```
nyasacare
├─ .gitignore
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ admin
│  ├─ extensions.py
│  ├─ main
│  │  ├─ __init__.py
│  │  └─ routes.py
│  ├─ models
│  │  ├─ base_model.py
│  │  └─ user.py
│  ├─ provider
│  ├─ static
│  │  ├─ responsive.css
│  │  └─ style.css
│  ├─ templates
│  │  ├─ index.html
│  │  └─ login.html
│  └─ user
│     ├─ __init__.py
│     └─ routes.py
├─ config.py
├─ notes.md
└─ tests

```