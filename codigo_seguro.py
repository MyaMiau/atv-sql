import sqlite3

# Criando banco de dados e tabela
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")

# Função de login (Segura contra Injeção SQL)
def secure_login(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return "Login bem-sucedido!" if result else "Login falhou!"

# Inserir dados via terminal
user_input = input("Digite o nome de usuário: ")
password_input = input("Digite a senha: ")

result = secure_login(user_input, password_input)  
print(result)

connection.close()
