from flask import Fask, redirect, url_for
app = Flask(__name__)
#ROOT
@app.route('/')
def root():
	return "The 'Home' Page"
#ROUTES FOR FORUM PAGES
@app.route("/general/")
def general():
	return "General forum page"

@app.route("/welcome/")
def welcome():
	return "The introduction forum page"

@app.route("/rumours/")
def rumours():
	return "The rumour forum page"

@app.route("/matchthreads/")
def match():
	return "Upcoming fixture forum page"

#ROUTES FOR LOGIN/LOGOUT
@app.route("/login")
def login():
	return "LOGIN ROUTE"
@app.route("/register")
def register():
	return "REGISTER ROUTE"

#PRIVATE ROUTS
@app.route("/membersarea")
def membersarea():
	# TEST FOR USER LOGIN
	#
	# IF USER NOT LOGGED IN REDIRECT TO LOGIN PAGE
	return redirect(url_for('login'))

#ERROR HANDLING
@app.errorhandler(404)
def page_not_found(error):
	return "THAT PAGE DOESN'T EXIST YOU WEAPON", 404
#TEST(replace '404' with error code required)
def forceerror():
	abort(404)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
