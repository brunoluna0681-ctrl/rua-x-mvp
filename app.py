from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista em memória para simular o banco de dados das ocorrências do MVP
ocorrencias = []

@app.route('/')
def index():
    return render_template('nova_ocorrencia.html', ocorrencias=ocorrencias)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    tipo = request.form.get('tipo')
    descricao = request.form.get('descricao')

    if tipo and descricao:
        ocorrencias.append({'tipo': tipo, 'descricao': descricao})

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)