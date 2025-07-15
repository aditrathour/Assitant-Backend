# Import the Flask class from the flask library
from flask import Flask

# Create a Flask web application instance
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses it to know where to look for resources like templates and static files.
app = Flask(__name__)

# This is a "route decorator". It tells Flask that the function directly below it
# should be executed when someone accesses the root URL ("/") of your web server.
@app.route('/')
def hello_assitant_backend():
    """
    This function handles requests to the root URL.
    It simply returns a string that will be displayed in the web browser.
    """
    return 'Hello from your Assitant-Backend! This is a simple start.'

# This block ensures that the Flask application runs only when the script is executed directly
# (not when it's imported as a module into another script).
if __name__ == '__main__':
    # app.run() starts the development server.
    # debug=True: This enables debug mode. It means:
    #   1. The server will automatically reload if you make changes to your code.
    #   2. It provides a debugger in the browser if an error occurs, which is super helpful for learning.
    # port=5000: This specifies which port the server will listen on. 5000 is a common default for Flask.
    app.run(debug=True, port=5000)
  
