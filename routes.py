from flask import Flask, redirect, render_template, request

app = Flask(__name__)
import models as DatabaseHandler

app.secret_key = '41o3190fsdlm8ofdvbm0934j'


#ROOT
@app.route('/')
def root():
	return render_template('/home.html')

@app.route('/recipes')
def recipes():
	return render_template('/recipes.html')

@app.route('/unitconversion')
def unitconversion():
	return render_template('/unitconversion.html')

@app.route('/liquidcups')
def liquidcups():
	return render_template('liquidcups.html')

@app.route('/poundsounces')
def poundsounces():
	return render_template('poundsounces.html')

#LOGIN/REGISTER ROOTS
@app.route('/login', methods=["GET","POST"])
def login():

	if request.method == "POST":
		
		attempted_username = request.form['username']
		attempted_password = request.form['password']

	return render_template('login.html')

@app.route('/register', methods=["GET","POST"])
def register():
	if request.method == "POST":
		attempted_username = request.form['username']
		attempted_password = request.form['password']
		attempted_email = request.form['email']
		DatabaseHandler.insertUser(attempted_username, attempted_password, attempted_email)

	return render_template('/register.html')	
@app.errorhandler(404)
def page_not_found(error):
	return "Page doesn't exist", 404


if __name__ == "__main__":
	app.run(host='0.0.0.0:80', debug=True)
