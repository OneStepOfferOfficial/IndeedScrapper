# all the webpage contents in this example are included in the return statements
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session: # "session" caches some info on the server side
        return 'Logged in as %s' % escape(session['username']) # escape function: automatically transfer the escape characters
    return 'You are not logged in' # the return statement is included in the response body

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p>user name: <input type=text name=username>
            <p>password:  <input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' 

if __name__ == '__main__': 
   app.run(port=5001, debug=True) # application will start listening for web request on port 5000