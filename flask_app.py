from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
@app.route('/')
def mostra_inicio():
    return render_template('inicio.html')


@app.route('/login')
def mostra_login():
    return render_template('login.html')

@app.route('/contato')
def mostra_login():
    return render_template('contato.html')


## Para rodar o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')