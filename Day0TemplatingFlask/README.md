# Flask Management System

Step by Step Guide to follow through the Project from basics.

## Setup Virtual Environment Firstly
We need to install virtual environment wrapper which gives access to `workon` to setup virtual environment so after installation and setting up path we can then switch between virtual environment to setup our system.

### Creating a virtual Environment
```
// To list down all the Virtual Environments
$ workon

//to create a new virtual environment named `elevtive2023env`
$ mkvirtualenv elective2023env

//to go inside of the virtual environment
$ workon elective2023env

//to get out of the virtual environment
$ deactivate
```
Creating a Virtual Environment provides us dedicated workspace for the project and is a good practice while working on Flask or any other frameworks.

### Viewing Packages and Use of `requirements.txt`    
Just like `package.json` in JavaScript, it is equivalent to `requirements.txt` in Python
```
//to view all the packages installed
$ pip freeze

//to make requirements.txt file by pasting all the installed packages
$ pip freeze > requirements.txt
```
If we are pushing any Flask Project to VCS like Git/Github then we must add `requirements.txt` file.

### Setting up Flask Server
Inside Virtual Environment `elective2023env`, install flask:
```
$ pip install Flask
```
Then we created a file named `app.py` in root and also created a folder named `templates` inside which we keep all the necessary files for the route.

```
from flask import Flask, render_template
 
//we need to use __ before and after name
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('pages/home.html')
    //render_template renders file inside of templates folder
 ```
Now, to run the server
```
$ python app.py
```
Now the server is live and we can start working on the project.
<hr>
<hr>

### Some Notes to remember about Templates
- templates are made so that we can reuse the same functionality of the code in frontend side too that decreases the hassle of backend  developer
- we first clone a Admin Template of our choice and then take out selective folders and files usually index.html, login.html, register.html > templates folder & other JS/CSS/img/scss/vendor folder > static folder
- Here, we have used {%block variable%}{%endblock%}  which is a Jinga template engine


