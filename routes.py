import ConfigParser
from flask import Flask, redirect, url_for, render_template, session
from config import Config

app = Flask(__name__)
app.secret_key = 'sd3.4=109ga.klma3,420-4123'

app.config.from_object(__name__)


#ROOT
@app.route('/')
def index():
	return render_template('./home.html')

@app.route('/session/write/<name>/')
def write(name=None):
	session['name'] = name
	return 'Wrote %s into "name" key of session' % name

@app.route('/session/read/')
def read():
	try:
		if(session['name']):
			return str(session['name'])
	except KeyError:
		pass
	return 'No session variable set for "name" key'

@app.route('/session/remove/')
def remove():
	session.pop('name', None)
	return "Removed key 'name' from session"

@app.route('/config/')
def config():
	s = []
	s.append('debug:'+app.config['DEBUG'])
	s.append('port:'+app.config['port'])
	s.append('url:'+app.config['url'])
	s.append('ip_address:'+app.config['ip_address'])
	return ', '.join(s)

def init(app):
	config = ConfigParser.ConfigParser()
	try:
		config_location = "etc/defaults.cfg"
		config.read(config_location)
		app.config['DEBUG'] = config.get("config", "debug")
		app.config['ip_address'] = config.get("config", "ip_address")
		app.config['port'] = config.get("config", "port")
		app.config['url'] = config.get("config", "url")
	except:
		print "could not read configs from: ", config_location


#ROUTES
@app.route("/general/")
def general():
	return "Gneral forum pa"

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
	init(app)
	app.run(host.config['ip_address'], port=int(app.config['port']), debug=True)
