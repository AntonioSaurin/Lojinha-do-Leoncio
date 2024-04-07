import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='leoncioStore'
)

cursor = db.cursor()

where = input("Digite o nome do item a ser alterado: ")
value = input("Digite o novo valor do item: ")
role = input("Digite a nova função do item dentre as já citadas anteriormente: ")

sql = "UPDATE itens SET value = %s, role = %s WHERE description = %s LIMIT 1"
values = (value, role, where)

try :
    cursor.execute(sql, values)
    db.commit()
except :
    print("Ocorreu um erro durante a atualização!")
    input("Aperta ENTER para fechar o programa!")
else :
    print("Atualização feita com sucesso!!")
    print(cursor.rowcount, "linhas afetadas!!")