from flask import Flask, request, render_template, redirect, url_for, session, flash
from db import create_connection, create_table, db_file  # Importa a função para criar conexão com o SQLite

import base64
import os
from flask import jsonify
from datetime import datetime
from usuario.usuario import usuario_bp
from produto.produto import produto_bp

app = Flask(__name__)


app.register_blueprint(usuario_bp)
app.register_blueprint(produto_bp)
# Quando precisar da conexão
app.secret_key = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
conn = create_connection(db_file)  # Cria a conexão com o banco de dados
if conn:  # Verifica se a conexão foi bem-sucedida
    create_table(conn)  # Chama a função para criar as tabelas
    conn.close()  # Fecha a conexão


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Obtém a conexão com o banco de dados
        conn = create_connection(db_file)  # Passa db_file como argumento
        cursor = conn.cursor()

        # Executa a consulta para verificar se o usuário existe
        cursor.execute("SELECT senha FROM usuarios WHERE username = ?;", (username,))  # Corrigido para SQLite
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        # Verifica se o usuário existe e se a senha está correta
        if user and user[0] == password:
            session['username'] = username  # Armazena o nome de usuário na sessão
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('registrar_venda'))  # Redireciona para a tela de registrar venda
        else:
            flash('Usuário ou senha incorretos!', 'danger')

    return render_template('login.html')

@app.route('/vendas')
def vendas():
    connection = create_connection(db_file)
    cursor = connection.cursor()

    # Consulta para obter vendas do dia
        # Consulta para obter vendas do dia
    query = """
    SELECT produto, quantidade, preco, data_venda
    FROM vendas
    WHERE DATE(data_venda) = CURRENT_DATE
    """
    cursor.execute(query)
    vendas_do_dia = cursor.fetchall()

    # Formata a data para um formato legível
    vendas_formatadas = [
        (
            produto,
            quantidade,
            preco,
            data_venda.strftime("%d/%m/%Y %H:%M:%S")  # Formato desejado
        )
        for produto, quantidade, preco, data_venda in vendas_do_dia
    ]

    cursor.close()
    connection.close()

    return render_template('vendas.html', vendas=vendas_formatadas)

@app.route('/registrar_venda', methods=['GET', 'POST'])
def registrar_venda():
    # Aqui você pode adicionar a lógica para registrar uma venda
    return render_template('registrar_venda.html')

@app.route('/produtos_pagina', methods=['GET'])
def listar_produtos_json():  # Mantenha esse nome para a função, se você preferir
    try:
        conn = create_connection(db_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, nome FROM produtos;")
        produtos = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(produtos)  # Retornar produtos como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/seguir_para_produtos')
def produtos():
    return render_template('produto.html')  # Inclua o caminho correto para o arquivo



if __name__ == '__main__':
    app.run(debug=True)
