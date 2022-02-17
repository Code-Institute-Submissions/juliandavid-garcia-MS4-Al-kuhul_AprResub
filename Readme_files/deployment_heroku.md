### 5.1 **Heroku deployment**
- **Go to Heroku.com, log in and create a new app**

![folder name](/Readme_images/1-create-app.JPG)

- **Name your project a choose your closest region**

![folder name](/Readme_images/2-nameapp.JPG)

- **In the resources tab choose Postgres database** 

![folder name](/Readme_images/3-postgres.JPG)

- **Select  the free plan for this project** 

![folder name](/Readme_images/4-free-version.JPG)

- **Go back to Gitpod and and install dj_database_url, and psycopg2 (Do not forget to freeze requirementes after this!)** 

![folder name](/Readme_images/5-install-psycopg2-binary.jpg)

- **In settings.py import the dj_database_url** 

![folder name](/Readme_images/6_import_database.JPG)

- **Comment out the default Database configuration and replace the default database with a call to dj_database_url.parse
And give it the database URL from Heroku** 

![folder name](/Readme_images/7-Database.JPG)

- **The  DATABASE URL is located in Heroku settings** 

![folder name](/Readme_images/8-database_url_key.JPG)

- **Migrate the changes to set up the database** 

![folder name](/Readme_images/9-migrations.JPG)

- **Load your data** 

![folder name](/Readme_images/10-loaddata.JPG)


- **Create a super user** 

![folder name](/Readme_images/11-superuser.JPG)

- **Remove Heroku database config from setting and uncomment the original so our database URL doesn't end up in version control.** 

![folder name](/Readme_images/12-data-remove.JPG)

- **Use an if statement in settings.py So that when our app is running on Heroku where the database URL environment variable will be defined. We connect to Postgres and otherwise, we connect to sequel light.** 

![folder name](/Readme_images/13-data-if-stament.JPG)

- **Install gunicorn, which will act as our webserver.
And freeze that into our requirements file.** 

![folder name](/Readme_images/14-gunicorn-n-freeze.JPG)

- **Create an Procfile add add a web dyno.
Which will run gunicorn and serve our django app. eventually login heroku** 

![folder name](/Readme_images/15-procfile.JPG)

- **By using Heroku config set, disable collectstatic equals 1
So that Heroku won't try to collect static files when we deploy.** 

![folder name](/Readme_images/16-disabel-collecstatic.JPG)

- **Add the hostname of our Heroku app to allowed hosts in settings.py** 

![folder name](/Readme_images/17-Allowed-HOST.JPG)

- **Commit, push and git push heroku main**

- **In heroku go to the deploy tab and select the option "connect to github"** 

![folder name](/Readme_images/18-connect-heroku.JPG)

- **Search your depository and connect your project and enable the automatic deplyment from guthub** 

![folder name](/Readme_images/19-automatic-deploy.JPG)

- [Back to read me](/README.md)