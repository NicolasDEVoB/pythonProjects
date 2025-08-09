from flask import Flask, render_template, redirect, request, url_for



app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def processa_login():
    if request.method == 'POST':
        email = request.form.get('email').strip().lower()
        senha = request.form.get('senha')
        print(f'Email recebido: {email}, Senha recebida: {senha}')
        if email == 'admin@gmail.com' and senha == 'adimin':
            print('Login bem-sucedido. Redirecionando para /home')
            return redirect(url_for('inicio'))
        else:
            print('Login falhou. Redirecionando para /')
            return redirect(url_for('login'))
    else:
        print('Requisição GET em /login. Redirecionando para /')
        return redirect(url_for('login'))


@app.route('/home')
def inicio():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
