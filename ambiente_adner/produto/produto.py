from flask import Blueprint, render_template, request, flash, redirect, url_for
from db import create_connection  # Função de conexão com o banco de dados

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/criar_produto', methods=['GET', 'POST'])
def criar_produto():
    conn = create_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']

        try:
            cursor.execute("INSERT INTO produtos (nome, descricao, preco) VALUES (%s, %s, %s);", (nome, descricao, preco))
            conn.commit()
            flash('Produto criado com sucesso!', 'success')
            return redirect(url_for('produto.listar_produtos'))
        except Exception as e:
            print(f"Erro ao criar produto: {e}")
            flash('Erro ao criar produto. Tente novamente.', 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('produto.html')

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, descricao, preco FROM produtos;")
    produtos = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('produto.html', produtos=produtos)


@produto_bp.route('/editar_produto/<int:id>', methods=['POST'])
def editar_produto(id):
    conn = create_connection()
    cursor = conn.cursor()

    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']

    try:
        cursor.execute("UPDATE produtos SET nome = %s, descricao = %s, preco = %s WHERE id = %s;", (nome, descricao, preco, id))
        conn.commit()
        flash('Produto alterado com sucesso!', 'success')
    except Exception as e:
        print(f"Erro ao alterar produto: {e}")
        flash('Erro ao alterar produto. Tente novamente.', 'danger')
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('produto.listar_produtos'))  # Ajustar aqui

@produto_bp.route('/excluir_produto/<int:id>', methods=['POST'])
def excluir_produto(id):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM produtos WHERE id = %s;", (id,))
        conn.commit()
        flash('Produto excluído com sucesso!', 'success')
    except Exception as e:
        print(f"Erro ao excluir produto: {e}")
        flash('Erro ao excluir produto. Tente novamente.', 'danger')
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('produto.listar_produtos'))  # Ajustar aqui
