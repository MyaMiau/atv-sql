import sqlite3

# Banco de dados
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")


def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return "Login bem-sucedido!" if result else "Login falhou!"


user_input = input("Digite o nome de usuário: ")
password_input = input("Digite a senha: ")

result = login(user_input, password_input)  
print(result)

connection.close()

""" Neste caso vc pode utilizar admin' -- para fazer login, 
a senha vai ser ignorada e o banco de dados apenas verifica se existe um usuário com o nome admin. 
Como existe um usuário com esse nome no banco de dados, o login é bem-sucedido, mesmo que a senha fornecida seja incorreta."""