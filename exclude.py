import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='leoncioStore'
)

cursor = db.cursor()

sql = "DELETE FROM itens WHERE id = %s"
where = (1)

cursor.execute(sql, where)

db.commit()

print(cursor, " linhas deletadas")