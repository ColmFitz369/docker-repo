from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)
@app.route('/')
def index():
return 'Index Page'
@app.route('/hello')
def hello():
<<<<<<< HEAD
return 'Hello World'
@app.route('/user/<username>')
def show_user_profile(username):
# show the user profile for that user
return 'User %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
return 'Post %d' % post_id
=======
    return "Hello World!"

@app.route("/")
def address():
    return "Dublin!"
  
@app.route("/")
def message():
    return "How are you?"

>>>>>>> e3545d81ac7e72b259f0cbf6387101363a955bbe
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
if request.method == 'POST':
f = request.files['file']
f.save('./uploads/'+f.filename)
return '',201
@app.route('/chkUploads')
def chk_uploads():
path = "./uploads/"
dirs = os.listdir( path )
f_str=""
for name in dirs:
f_str +=(str)(name)+"\n"
return f_str
@app.route('/eu1')
def run_eu1():
i=0
total=0
while i < 1000: #stop when we reach multiple bigger than 1000
if(i%5==0 or i%3==0): #ie if multiple of 5 or 3
total+=i #add multiple to cumulative tally
i+=1 #next number (will be used only if a valid multiple)
result=" "+(str)(total)+"\n"	
return result
@app.route('/eu2')
def run_eu2():
pre,fib,tally=0,1,0 #initialize variables, pre is last term fib is current
MAX=4000000 #4million is maximum value of a term
while fib <= MAX:
if(fib%2): tally+=fib #add to tally is fib term is even
pre,fib=fib,pre+fib #get new values for pre and fib
result=" "+(str)(tally)+"\n"
return result
if __name__ == "__main__":
app.run(host="0.0.0.0", debug=True)
