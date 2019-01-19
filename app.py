from flask import *
from databases import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")
@app.route('/shop')
def shopnow():
	return render_template("shop.html")
@app.route('/womens-tops')
def womens_tops():

	return render_template("womens_top.html")
@app.route('/contact')
def contactnow():
	return render_template("contact.html")
@app.route('/about')
def aboutnow():
	return render_template("about.html")
if __name__ == '__main__':
   app.run(debug = True)