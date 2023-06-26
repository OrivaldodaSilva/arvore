# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Arthur lucena lopes" # escreva seu nome
    idade = "1567238" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home():

    nome = "Rnnoy" # escreva seu nome
    idade = "5692076879" # escreva sua idade

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mãe")
def home():

    nome = "Giana" # escreva seu nome
    idade = "5692076879" # escreva sua idade

    return render_template('mãe.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.route("/Ryan")
def home():

    nome = "Ryan" # escreva seu nome
    idade = "5692076879" # escreva sua idade

    return render_template('Ryan.html' , nome = nome , idade = idade)


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
