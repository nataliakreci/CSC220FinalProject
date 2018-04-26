# CSC220FinalProject

This project builds a website called Click Clack Type, which encourages children to type , spell and learn how to type efficiently. The website opens up to a home page which lists all the pictures that are on the app. The side bar has a two playing options: "Play" mode and "Practice" mode. Both modes show an image, and record the type time once a player begins to type the name of the image. The Play mode records the time the player takes to type, as well as which words were correct and which were incorrect. The Practice mode does not record any performance measures, it is a place in which the player can practice and get better without changing their results. 

The entire code for Click Clack Type is downloaded as a file. The main file is called the "flask_app" file, which contains the database, html code, css code, as well as the packages needed to run the website. The "app" file contains the templates and static information. The templates contain the html for every page in Click Clack Type, and the static file contains the pictures of the objects, and the logo. The routes file links the webpage functions. 

To run Click Clack Type, you need to have Flask installed, because it is a Flask project. 

To install Flask, follow the directions at http://flask.pocoo.org/docs/0.12/installation/.
There are two options to install Flask:
1) to install Flask using your terminal, type:   $ pip install Flask
2) to install a virtual environment as well (not necessary for this project): $ sudo pip install virtualenv

Two packages will be needed as well.
3) $ pip install flask_sqlalchemy
4) $ pip install flask_migrate

Once Flask is installed, you can run the project. These are the steps to run the app:
1) Enter the correct file path. First, the main folder, then the flask_app folder inside. Type:
  cd CSC220FinalProject
  cd flask_app
3) Once you are in the flask_app folder, run the app by typing into the terminal:
  $ export FLASK_APP=clickclacktype.py
4) Followed by:
  $ flask run
5) Follow the link prompted in the terminal, or just copy this link into your browser: 
  http://127.0.0.1:5000/ 
6) ENJOY THE GAME!
