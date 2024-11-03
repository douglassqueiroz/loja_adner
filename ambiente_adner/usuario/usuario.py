from flask import Blueprint, render_template, request, flash, redirect, url_for
from db import create_connection, db_file  # Verifique se a função está nomeada corretamente

# Cria um blueprint para o módulo de usuário
usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/criar_usuario', methods=['GET', 'POST'])
def criar_usuario():
    conn = create_connection(db_file)  # Certifique-se de que a conexão está sendo criada corretamente
    cursor = conn.cursor()

    # Buscar usuários para listar
    cursor.execute("SELECT id, username FROM usuarios;")
    usuarios = cursor.fetchall()

    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']
        print(f"Usuário: {username}")
        print(f"Senha: {senha}")

        try:
            cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?);", (username, senha))
            conn.commit()
            flash('Usuário criado com sucesso!', 'success')
            return redirect(url_for('usuario.criar_usuario'))  # Redireciona após sucesso
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
            flash('Erro ao criar usuário. Tente novamente.', 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('criar_usuario.html', usuarios=usuarios)  # Passa a lista de usuários para o template

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conn = create_connection(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM usuarios;")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('criar_usuario.html', usuarios=usuarios)

@usuario_bp.route('/atualizar_usuario/<int:user_id>', methods=['GET', 'POST'])
def atualizar_usuario(user_id):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']
        
        try:
            cursor.execute("UPDATE usuarios SET username = ?, senha = ? WHERE id = ?;", (username, senha, user_id))
            conn.commit()
            flash('Usuário atualizado com sucesso!', 'success')
            return redirect(url_for('usuario.listar_usuarios'))
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            flash('Erro ao atualizar usuário. Tente novamente.', 'danger')
        finally:
            cursor.close()
            conn.close()
    
    cursor.execute("SELECT username, senha FROM usuarios WHERE id = ?;", (user_id,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('atualizar_usuario.html', usuario=usuario)

@usuario_bp.route('/deletar_usuario/<int:user_id>', methods=['POST'])
def deletar_usuario(user_id):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM usuarios WHERE id = ?;", (user_id,))
        conn.commit()
        flash('Usuário deletado com sucesso!', 'success')
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        flash('Erro ao deletar usuário. Tente novamente.', 'danger')
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('usuario.listar_usuarios'))