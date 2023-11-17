# Nyasa Care

### Description
<p> Nyasa Care is a multi-user platform where health service providers list their services and allow members of the public to book for their services. </p>
<p>This project was tested on Ubuntu 20.04</p>

### Authors
1. Prince Mawonde
2. Junior Sibusiso Ngondo
3. Michael Kazembe

### Packages
- Flask
- Flask-SQLAlchemy
- python-dotenv 
- Flask-Migrate 
- flask_validator 
- psycopg2-binary
- email-validator
- Flask-Bcrypt
- Flask-Login
- Flask-wtf


### Setup
1. #### Install a Database on your local machine (for local testings)
- We used postgresql for this project see ```notes.md file```
- Create a database call it any name you want. We called ours nyasacare 

2. #### Setting up the environment 
- cd into nyasacare and run  ``` python3 -m venv .venv``` in the terminal to create a virtual environment
- run ```. .venv/bin/activate ``` to activate the environment . NB to deactivate the virtual 

3. #### Install packages
- pip install python-dotenv flask flask-sqlalchemy Flask-Migrate flask_validator psycopg2-binary

### Environment variables 
- See the ```.env.example``` file


### How to run the app

### Start the Database if running locally or on custom servers

- `sudo service postgresql status` for checking the status of your database.
- `sudo service postgresql start` to start running your database.
- `sudo service postgresql stop` to stop running your database.

#### Create Tables in your database

###### your might need to Delete the migrations folder first
$ flask db init 
$ flask db migrate
$ flask db upgrade $


#### Run using the run.py file
- Simply type `python3 run.py` 


#### Run using the create_app

1. Set the app package (because it has __init__.py) as the place where Flask should look for the create_app() factory function:  ```export FLASK_APP=app ```
2. Set the FLASK_ENV environment variable to run the application in development mode: ```export FLASK_ENV=development ```
3.  Run the application: ``` flask run```
4.  To Run the Server with specific host and port  ```flask run -h HOSTNAME -p PORTNUMBER``` e.g flask run -h 127.0.0.1 -p 5001
5. To Run the Server with Automatic Restart When Changes Occur ```FLASK_DEBUG=1 flask run```  or simply `flask --debug run`




### Folder Structure


```
nyasacare
├─ .gitignore
├─ .vscode
│  └─ settings.json
├─ README.md
├─ app
│  ├─ __init__.py
│  ├─ admin
│  │  ├─ __init__.py
│  │  └─ routes.py
│  ├─ extensions.py
│  ├─ main
│  │  ├─ __init__.py
│  │  ├─ forms.py
│  │  └─ routes.py
│  ├─ models
│  │  ├─ __init__.py
│  │  └─ user.py
│  ├─ provider
│  ├─ static
│  │  ├─ img
│  │  │  ├─ doc1.jpg
│  │  │  ├─ doc2.jpg
│  │  │  ├─ doc3.jpg
│  │  │  ├─ doc4.jpg
│  │  │  ├─ doc5.jpg
│  │  │  ├─ doc6.jpg
│  │  │  ├─ doc7.jpg
│  │  │  └─ nurse.jpg
│  │  ├─ index.css
│  │  ├─ responsive.css
│  │  └─ style.css
│  ├─ templates
│  │  ├─ admin
│  │  │  └─ index.html
│  │  ├─ base.html
│  │  ├─ index.html
│  │  ├─ login.html
│  │  ├─ provider
│  │  │  └─ index.html
│  │  ├─ register.html
│  │  └─ user
│  │     ├─ history.html
│  │     ├─ index.html
│  │     └─ layout.html
│  └─ user
│     ├─ __init__.py
│     ├─ controllers.py
│     └─ routes.py
├─ app.db
├─ config.py
├─ migrations
│  ├─ README
│  ├─ alembic.ini
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
│     └─ 024f068c9445_.py
├─ notes.md
├─ run.py
└─ tests

```