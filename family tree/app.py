# importando os módulos da biblioteca flask
from flask import Flask, render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Maria" # escreva seu nome
    idade = "14 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home1():
    
    nome = "Carlos"
    idade = "?? anos"
    
    return render_template('pai.html', nome = nome, idade = idade)

# defina a rota para a página da mãe
@app.route("/mae")
def home2():
    
    nome = "Carolina"
    idade = "?? anos"
    
    return render_template('mae.html', nome = nome, idade = idade)


# defina a rota para a página do amigo
@app.route("/amigo")
def home3():
    
    nome = "josefo"
    idade = "14 anos"
    
    return render_template('amigo.html', nome = nome, idade = idade)


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
