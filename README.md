#  Web CV
The biography is presented in a form different from the biographical one - the information is exchanged in separate thematic blocks marked with headings or sub-titles: personal data, professional experience, education, projects, personal preferences (hobbies, interests, etc.).

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development.
##### Prerequisites
What things you need to install the software and how to install them.
Web CV requires to run:
- Django (ver. 1.11+)
- Python (ver. 3.0+)
#### Installation
##### 1. virtualenv / virtualenvwrapper
You should already know what is [virtualenv](https://virtualenv.pypa.io/en/stable/), preferably [virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper) at this stage. So, simply create it for your own project, where projectname is the name of your project:
```
$ mkvirtualenv --clear projectname
```
##### 2. Download
Now, you need the django-sample-app project files in your workspace:
```
$ cd /path/to/your/workspace
$ git clone https://github.com/hubert-hernoga/my_web_cv.git
```
##### 3. Requirements
Right there, you will find the requirements.txt file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:
```
$ pip install -r requirements.txt
```

###### To start the project you only must:

- start local server
```
/<project folder> $ python manage.py runserver 0.0.0.0:8000
```
- open http://127.0.0.1:8000/ to the browser

## Deployment
You can deploy project on ```heroku``` server (then you can use only ```PostgreSQL```).
More information about deployment you can find here:
https://devcenter.heroku.com/articles/getting-started-with-python#introduction

### Technologies used

* Python (Django),
* JavaScript + JQuery,
* HTML + CSS.

