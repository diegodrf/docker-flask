from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('diego'))

@app.route('/diego')
def diego():
    nome = 'Diego Rodrigues de Faria'
    return render_template('diego.html', nome=nome)

@app.route('/flask')
def flask():
    return render_template('flask.html')

@app.route('/zabbix')
def zabbix():
    return redirect('http://0.0.0.0')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

