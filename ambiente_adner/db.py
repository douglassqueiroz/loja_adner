import sqlite3
from sqlite3 import Error
db_file = "loja_adner.db"

def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("Conexão com o banco de dados realizada com sucesso.")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def create_table(connection):
    """Create tables in the SQLite database."""
    try:
        cursor = connection.cursor()
        
        # Criação da tabela usuarios
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            senha TEXT
        );
        """)
        print("Tabela 'usuarios' criada ou já existe.")

        # Criação da tabela produtos
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            descricao TEXT,
            preco REAL,
            quantidade INTEGER
            
        );
        """)
        print("Tabela 'produtos' criada ou já existe.")
        
        connection.commit()
        print("Tabelas criadas com sucesso.")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()  # Garante que o cursor seja fechado

# Exemplo de uso
if __name__ == "__main__":
    db_file = "loja_adner.db"  # Nome do arquivo do banco de dados SQLite
    conn = create_connection(db_file)    # Criação da conexão

    if conn:  # Verifica se a conexão foi bem-sucedida
        create_table(conn)  # Criação das tabelas
        conn.close()  # Fecha a conexão
    else:
        print("Erro ao criar a conexão com o banco de dados.")
