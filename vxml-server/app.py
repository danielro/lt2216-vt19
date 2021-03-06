from flask import Flask, render_template, make_response, send_from_directory
app = Flask(__name__)

temp = '13'

@app.route('/lab1')
def lab1():
    vxml = render_template('lab1/lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1_book')
def lab1_book():
    vxml = render_template('lab1/lab1_book.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1_delays')
def lab1_delays():
    vxml = render_template('lab1/lab1_delays.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab1_menu')
def lab1_menu():
    vxml = render_template('lab1/lab1_menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab2_quotes')
def lab2_quotes():
    vxml = render_template('lab2_quotes.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab2_home')
def lab2_home():
    vxml = render_template('lab2_home.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab3')
def lab3():
    vxml = render_template('lab3.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab3_sound_of_dialogue')
def lab3_sound_of_dialogue():
    vxml = render_template('lab3_sound_of_dialogue.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab4')
def lab4():
    vxml = render_template('lab4.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab4_book')
def lab4_book():
    vxml = render_template('lab4_book.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab4_delays')
def lab4_delays():
    vxml = render_template('lab4_delays.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)
