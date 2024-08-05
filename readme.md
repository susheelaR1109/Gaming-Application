# Game App

## App creation steps
##### install Django 
pip install Django

##### From the command line, cd into a directory where you’d like to store your code, then run the following command:
django-admin startproject mysite

##### Change into the outer mysite directory, if you haven’t already, and run the following commands:
python manage.py runserver

###### the server’s running, visit http://127.0.0.1:8000/ with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off.


## Creating the Game app
##### To create your app, make sure you’re in the same directory as manage.py and type this command:
python manage.py startapp game

## Creating the Vue app
##### To create the vue app, u need to be in the parent folder and not inside django folder that was created
npm install -g @vue/cli
vue create app_name

cd project_name
npm install
npm run dev
