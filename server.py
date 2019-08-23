from flask import Flask, render_template, request, redirect, url_for, flash
from cripto import sha_256

app = Flask(__name__)
app.secret_key = 'mysecretekey'

@app.route('/')
def index():
    #print(sha_256('sdfsdf'))
    return render_template('index.html')

@app.route('/info')
def info():
    #print(sha_256('sdfsdf'))
    return render_template('info.html')

@app.route('/shaEcription', methods = ['POST'])
def shaEcription():
    if request.method == 'POST':
        textus = request.form['texto']
        responses = list(sha_256(textus))
        resOff = " - ".join(responses)
        flash('Texto a Encriptar: \n' + textus)
        flash('SHA-256: \n'+ resOff)
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port = 3000, debug = True)