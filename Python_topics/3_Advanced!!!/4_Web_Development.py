# ----------------------------------------------------------------------
# Web Development in Python
# ----------------------------------------------------------------------
# Python offers powerful web frameworks like Flask and Django for building web applications.
# - Flask: A lightweight and flexible framework, suitable for small to medium projects.
# - Django: A robust and full-featured framework for large applications.

# Below, we'll focus on Flask for simplicity, but similar concepts apply to Django.

# ----------------------------------------------------------------------
# 1. Flask Framework: Building a Simple Web Application
# ----------------------------------------------------------------------
# Flask is a microframework that provides tools to build web apps quickly and efficiently.
# Install Flask: `pip install flask`

from flask import Flask

app = Flask(__name__)  # Create a Flask app instance

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to Flask Web Development!"

# Define another route
@app.route('/about')
def about():
    return "This is the About page."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Start the development server

# Run this script and visit http://127.0.0.1:5000 in your browser.

# ----------------------------------------------------------------------
# 2. Building RESTful APIs with Flask
# ----------------------------------------------------------------------
# RESTful APIs are used to interact with data using HTTP methods like GET, POST, PUT, DELETE.
# Install Flask's extensions for RESTful APIs: `pip install flask-restful`

from flask import request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Example in-memory data store
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Define a Resource for users
class UserList(Resource):
    def get(self):
        """GET all users."""
        return jsonify(users)

    def post(self):
        """POST a new user."""
        data = request.json  # Get JSON data from the request body
        new_user = {
            "id": len(users) + 1,
            "name": data["name"],
            "email": data["email"]
        }
        users.append(new_user)
        return jsonify(new_user), 201

# Add the resource to the API
api.add_resource(UserList, '/users')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

# Test with curl or Postman:
# GET all users: `curl http://127.0.0.1:5000/users`
# POST a new user: `curl -X POST -H "Content-Type: application/json" -d '{"name":"Charlie","email":"charlie@example.com"}' http://127.0.0.1:5000/users`

# ----------------------------------------------------------------------
# 3. Templating with Jinja2 in Flask
# ----------------------------------------------------------------------
# Flask uses the Jinja2 templating engine to render dynamic HTML pages.
# Jinja2 syntax allows embedding Python code in HTML files.

from flask import render_template

# Flask expects templates to be stored in a `templates` directory.
# Example: Create `templates/home.html` with the following content:
"""
<!DOCTYPE html>
<html>
<head>
    <title>Flask Template</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    <p>This is a dynamic web page rendered using Jinja2.</p>
</body>
</html>
"""

@app.route('/template/<name>')
def template(name):
    return render_template('home.html', name=name)

# Run the app and visit: http://127.0.0.1:5000/template/John
# It will render the HTML with "Welcome, John!"

# ----------------------------------------------------------------------
# 4. Web Forms and Validation
# ----------------------------------------------------------------------
# Flask-WTF simplifies working with web forms and validation in Flask.
# Install Flask-WTF: `pip install flask-wtf`

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app.config['SECRET_KEY'] = 'secret_key'  # Required for CSRF protection

# Define a Flask-WTF form
class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()  # Create an instance of the form
    if form.validate_on_submit():  # Check if the form is submitted and valid
        name = form.name.data  # Get the submitted name
        return f"Hello, {name}!"
    return render_template('form.html', form=form)

# Create `templates/form.html` for the form:
"""
<!DOCTYPE html>
<html>
<head>
    <title>Flask Form</title>
</head>
<body>
    <h1>Enter Your Name</h1>
    <form method="post">
        {{ form.hidden_tag() }}  <!-- CSRF token -->
        {{ form.name.label }} {{ form.name(size=20) }}
        {{ form.submit() }}
    </form>
</body>
</html>
"""

# Run the app and visit: http://127.0.0.1:5000/form
# Enter your name and submit the form to see the result.

# ----------------------------------------------------------------------
# Summary: Flask Web Development
# ----------------------------------------------------------------------

# 1. **Flask Framework**:
#    - Lightweight and flexible.
#    - Define routes using `@app.route()`.

# 2. **Building RESTful APIs**:
#    - Use Flask-RESTful for creating RESTful APIs.
#    - Use HTTP methods (GET, POST, PUT, DELETE) for CRUD operations.

# 3. **Templating with Jinja2**:
#    - Use Jinja2 syntax to create dynamic HTML pages.
#    - Embed Python code in templates with `{{ ... }}`.

# 4. **Web Forms and Validation**:
#    - Use Flask-WTF for building forms and handling validation.
#    - Define forms with WTForms and render them in templates.

# Flask is suitable for small to medium projects. For larger applications, consider Django for its built-in features like ORM, admin panel, and user authentication.

