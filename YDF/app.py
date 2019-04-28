from flask import Flask, render_template, request
import requests

app = Flask('YDF')

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	# Extracting data from the form
	location = request.form['location']
	holidaytype = request.form['type']
	budget = request.form['budget']

	if location == 'beach':
		best_location=beaches[budget][holidaytype]
		return render_template('beach.html', best_location=best_location)

	if location == 'city':
		best_location=cities[budget][holidaytype]
		return render_template('city.html', best_location=best_location)

# Dictionaries
cities = {
	"cheap":{
		'party':'Copenhagen',
		'adventure':'Prague',
		'relax':'Budapest'
	},
	"medium":{
		'party':'Amsterdam',
		'adventure':'Barcelona',
		'relax':'Athens'
	},
	"expensive":{
		'party':'Berlin',
		'adventure':'Rome',
		'relax':'Florence'
	}
}

beaches = {
	"cheap":{
		'party':'Magaluf',
		'adventure':'Palma Majorca',
		'relax':'Faro'
	},
	"medium":{
		'party':'Ayia Napa',
		'adventure':'Crete',
		'relax':'Corfu'
	},
	"expensive":{
		'party':'Ibiza',
		'adventure':'Malta',
		'relax':'Santorini'
	}
}

@app.route("/signup",methods=["POST"])
def sign_up():
    form_data = request.form
    email = form_data["email"]
    send_simple_message(email)
 
    return render_template('mailsuccess.html')

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox14f3d6b8c57c4cf19fc731d8eff72b1f.mailgun.org/messages",
        auth=("api", "440828a956f0b6469860d8f06ffcafed-acb0b40c-648fef98"),
        data={"from": "YDF <mailgun@sandbox14f3d6b8c57c4cf19fc731d8eff72b1f.mailgun.org>",
              "to": [email],
              "subject": "Holiday deals",
              "text": "Here are some great holiday deals!"})

if __name__ == '__main__':
    app.run(debug=True)
