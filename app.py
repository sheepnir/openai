# Importing necessary modules from the Flask package
from flask import Flask, render_template

# Creating an instance of the Flask class. This instance will act as the WSGI application.
app = Flask(__name__)

# Defining a route for the root URL ('/'). This route will be associated with the hello_world function.
@app.route('/')
def hello_world():
    # The function hello_world is called when the root URL is accessed.
    # render_template is a Flask function that renders a template.
    # 'index.html' is the HTML template file to be rendered.
    # 'message' is a variable that is passed to the template. 
    # Its value will be accessible in the template as {{ message }}.
    return render_template('index.html', message='Hello from Flask')

# Checking if this script is executed as the main program and not imported as a module.
if __name__ == '__main__':
    # Running the Flask application.
    # debug=True enables a debugger and reloader for easy debugging during development.
    app.run(debug=True)
