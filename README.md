# Storefinder   
A web app using Flask for the API and Vue.js for the frontend to let customers find store locations based on their inputted town, city or postcode.

![storefinder app demo](https://github.com/helenodia/storefinder/blob/main/client/public/images/storefinder-demo.gif)

## Dependencies
### API
- Python 3.9
- Pip
- Pipenv
- Flask
- Flask-cors

### Web app
- Vue 3
- Axios
- Lodash

## Setup
Download and unzip the main `storefinder` project folder.

Then follow the below instructions to set up the Flask API and Vue app.

### API
In your terminal:

    $ cd storefinder/api

Make sure you have Python 3.x and Pipenv installed:

    $ python --version
    $ pipenv
Then run the following commands in a terminal window to start your virtual environment, install required dependencies and run the API:

    $ pipenv shell
    $ pipenv install 
    $ FLASK_ENV=development pipenv run flask run # Start development server
    (env)$ python3 app.py
   Test the endpoints at http://127.0.0.1:5000/ either in your browser or using [Postman](https://www.postman.com/).
   
   To stop `appy.py`, use `ctrl + c`. 
   To exit the virtual environment, use `ctrl + d`.
   
### Web app
In a new terminal window inside the app directory, run:

    $ cd storefinder/client
    $ npm install # Install dependencies
    $ npm run serve
Go to http://localhost:8080/ to see the app in your browser.

Now both parts of the app are running, you're ready to try out the search form.
