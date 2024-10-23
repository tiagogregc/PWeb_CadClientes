from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def cadclient():
    return render_template('cad_clientes.html')

@app.route('/inserir_cliente', methods=['POST'])
def inserir_usuario():
    cpf = request.form['txt_cpf']
    nome = request.form['txt_nome']
    cidade = request.form['txt_cidade']
    telefone = request.form['txt_telefone']
    db = mysql.connector.connect(host='201.23.3.86', user='usr_aluno', password='E$tud@_m@1$', port=5000, database = 'aula_fatec') ## Estabelece conexão com o banco de dados

    query = "INSERT INTO Tiago_Carvalho_tbClientes (cpf, nome, cidade, telefone) VALUES ( %s, %s, %s, %s)" 
    ##print query - para identificar o erro 
    ## %s representa que é uma variavel string
    valores = (cpf, nome, cidade, telefone)

    meucursor = db.cursor() ## para executar a conexão com o banco, precisamos de um cursor
    meucursor.execute(query, valores)
    db.commit() 
    return "foi"

app.run()