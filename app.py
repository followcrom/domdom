"""
How to connect Github with Atom: https://www.youtube.com/watch?v=6HsZMl-qV5k

How To Install Flask: https://phoenixnap.com/kb/install-flask
Create an Environment in Windows
py -3 -m venv <name of environment>

Activate the Environment on Windows:
<name of environment>\Scripts\activate

setx FLASK_APP "app.py"

Deactivate the Environment on Windows:
<name of environment>\Scripts\deactivate
"""


from flask import Flask, render_template, jsonify, request
from sqlalchemy import text
from database import engine, load_domdoms_from_db, load_domdom_from_db, add_to_db

app = Flask(__name__)  # Creating an object of Flask called app



@app.route('/')
def load_doms():
    domdoms = load_domdoms_from_db()
    return render_template('index.html',
                        domdoms=domdoms,
                        company_name='SchoFlow')

@app.route('/<id>')
def show_dom(id):
    domdom = load_domdom_from_db(id)
    if not domdom: # if job doesn't exsist
        return "Not Found", 404
    return render_template('quote.html', domdom=domdom)


@app.route('/api/wisdom/<id>') # an api page for a json list
def show_json(id):
    domdom = load_domdom_from_db(id)
    return jsonify(domdom)


@app.route('/sent', methods=['post'])
def send_wisdom():
    data = request.form
    add_to_db(data)
    # send an email
    # return jsonify(data)
    return render_template('submitted.html',
                            submission=data)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True) # running on local host
