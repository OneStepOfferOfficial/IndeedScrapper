# File name: hello_webapp.py 
from flask import Flask, render_template # include the flask library 

app = Flask(__name__) 

@app.route("/") 
def index(): 
   return "Hello, World!" 


@app.route("/plus") 
def test(): 
   return "This is test page" 

@app.route("/template") 
def show_template(): 
   return render_template('index.html', name="Alex")

@app.route('/displayprofile', methods=['GET'])
def showbio():    
    username = request.args.get('username')    
    age = request.args.get('age')    
    email = request.args.get('email')    
    hobbies = request.args.get('hobbies')    
    return render_template("profile.html",
                           username=username,                         
                           age=age,                          
                           email=email,                         
                           hobbies=hobbies)



@app.route('/post/<int:post_id>')
def show_post(post_id):
	app.logger.debug('Post %d is displayed' % post_id)
	return 'Post %d' % post_id

@app.route("/table-for-loop") 
def table_for_loop(): 
   return render_template('table.html', data={'row1': 'value1', 'row2': 'value2', 'row3': 2})

@app.route("/turn-on") 
def turn_on(): 
   return render_template('switch.html', turned_on= True)

if __name__ == '__main__': 
   app.run(port=5001, debug=True) # application will start listening for web request on port 5000