from flask import *
import sql
from wtforms import Form, BooleanField, TextField, PasswordField,StringField, validators
from wtforms import TextField
from wtforms.validators import DataRequired



   
   
app = Flask(__name__)





@app.route("/",methods = ['GET','POST'])
@app.route("/login",methods = ['GET','POST'])
def login():
	error = False
	if request.method == 'POST':
		if request.form['login'] =='admin' and request.form['pass'] =='admin':
			
			return redirect('welcome')
		else:
			name = request.form['login']
			
			return guest(name.upper())
		error = True	
	
	return render_template('login.html',error=error)
	
	
	
@app.route("/welcome",methods = ['GET','POST'])
def welcome():
	error=''
	query1 = sql.query1
	query2 = sql.query2
	if request.method == 'POST':
		 
		id = request.form['id'] 
		name = request.form['name']
		action = request.form['action']
		db_table = request.form['tables']
		error=choose_of_action(action,db_table,id,name)
	
	return render_template('welcome.html',error=error,query1=query1,query2=query2)

	
@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/guest")
def guest(name='Guest'.upper()):
	query = sql.query
	return render_template('guest.html',query=query,name=name)	

def choose_of_action(action,table,id,name):
	if action == 'add':
		error = sql.new_record(table,id,name)
	elif action == 'modify':
		error = sql.modify_record(table,id,name)
	elif action == 'delete':
		error = sql.delete_record(table,id,name=name)
	return error
	
			
	
if __name__ == "__main__":
    app.run(debug=True)