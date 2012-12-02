"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object(__name__)

if 'SECRET_KEY' in os.environ:
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
else:
    app.config['SECRET_KEY'] = 'this_should_be_configured'

###
# Routing for your application.
###

users = [
    'angelhack',
    'beerme',
    'sandwiches'
]

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/beerme')
def beerme():
    return render_template('beerme.html')

@app.route('/angelhack')
def angelhack():
    return render_template('angelhack.html')

@app.route('/filepickerio')
def filepickerio():
    return render_template('filepickerio.html')

@app.route('/firebase')
def firebase():
    return render_template('firebase.html')



@app.route('/recent')
def recent():
    return render_template('recent.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/cpp')
def cpp():
    return render_template('cpp.html')

@app.route('/java')
def java():
    return render_template('java.html')

@app.route('/go')
def go():
    return render_template('go.html')

@app.route('/perl')
def perl():
    return render_template('perl.html')

@app.route('/scala')
def scala():
    return render_template('scala.html')

@app.route('/javascript')
def javascript():
    return render_template('javascript.html')

@app.route('/objectivec')
def objectivec():
    return render_template('objectivec.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
