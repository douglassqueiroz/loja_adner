import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError

def create_connection():
    """Create a database connection to the PostgreSQL database."""
    connection = None
    try:
        connection = psycopg2.connect(
            dbname='postgres',   # Substitua pelo nome do seu banco de dados
            user='postgres',           # Seu usuário do PostgreSQL
            password='postgres',      # Sua senha do PostgreSQL
            host='localhost',
            port='5432'
        )
        print("Conexão com o banco de dados realizada com sucesso.")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

    return connection
