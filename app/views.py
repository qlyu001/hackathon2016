from flask import Flask, flash, redirect, render_template, request, session, abort
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
  user = {'nickname' : 'Melissa'}
  return render_template('index.html', **locals())
@app.route('/hello/<string:name>/')
def hello(name):
  return render_template('hello.html', **locals())
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', title='Sign In', form=form)