from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    return  render_template('index.html', title='home')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', title="About me")

@app.route('/certificates')
def skills():
    return render_template('certificates.html', title="Skills")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

@app.route('/resume')
def resume():
    return render_template('resume.html', title="Resume")

@app.route('/links')
def links():
    return render_template('links.html', title="Links")
