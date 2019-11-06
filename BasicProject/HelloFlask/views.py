from flask import render_template
from HelloFlask import app
from datetime import datetime

@app.route('/')
@app.route('/home')
def home():
	now=datetime.now()
	formatted_now=now.strftime("%A,%d %B,%Y at %X")

	return render_template(
		"/time/index.html",
		title='Hello Flask',
		message="Hello Flask !",
		content=" on "+formatted_now

		)