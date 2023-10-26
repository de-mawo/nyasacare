# Notes

#### Flask Project Folder Structure Layout
- <a href="https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/"> Small Project Layout </a> 
- <a href="https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html#folder-structure-for-a-flask-app">Medium Project Layout  </a>
- <a href="https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy"> Large Project Layout </a>

#### File permissions to save a File
sudo chown prince:admin templates/index.html     

#### Avoid typing sudo everytime 
- sudo chown username folder_you_want_to_work_on
- sudo chown -R your_username /nyasacare

### Installing Postgresql
- <a href="https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database"> On WSL/ Ubuntu </a>

#### To add uuid functionality to the ```id``` Column of every model
- Connect to your PostgreSQL database: You can do this using the psql
- Enable the uuid-ossp extension: Run the following SQL command to enable the extension:
```CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; ```
- Verify that the extension is enabled: You can check if the extension is enabled by running the following command:
```SELECT * FROM pg_extension WHERE extname = 'uuid-ossp'; ```
