from flask import Flask, render_template, request, url_for, session, redirect, flash
import models as dbHandler
import jinja2
import os


app = Flask(__name__, static_url_path="/static" '/static', static_folder='static')


@app.route('/', methods= ['GET', 'POST'])
def hello_books():
    if 'username' in session:
        #books = {"Python for bigginers": "100", "Python for Dummies": "50"}
        return render_template("userHome.html")
    else:
        message = None
        #flash("Please sign up; you don't have an account with us")
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']


        return render_template("index.html")



@app.route('/registration', methods=['GET', 'POST'])
def registration():
    messages = []

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # check username length
        if len(username) < 4:
            messages.append("Invallid username- usernames must be at least 8 characters in length.")
        if len(username) > 20:
            messages.append(
                "Invallid username- The entered username is too long. Usernames must be 20 characters or less in length.")

        # check password length
        if len(password) < 4:
            messages.append("Invallid password- passwords must be at least 8 characters long.")
        if len(password) > 20:
            messages.append(
                "Invallid password- The password you entered is too long. Passwords must not be longer than 20 characters in length.")

        # if no error messages
        if len(messages) != 0:
            # return registration page with new error message(s)
            return render_template('registration.html', messages=messages)

        if (username) == True:
            messages.append("UserAlready exists")
            return render_template('registration.html', messages=messages)
        else:
            # insert new user
            dbHandler.create_database()
            dbHandler.insertUser(username, password)
            session['username'] = username
            return render_template("index.html")

    return render_template('registration.html', messages=messages)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug= True)
