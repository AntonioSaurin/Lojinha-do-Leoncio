import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='leoncioStore'
)

cursor = db.cursor()

name = input("Digite o nome do item a ser inserido na loja: ")
while True:
    try: 
        value = int(input("Digite o valor do item a ser vendido: "))
    except:
        input("O valor deve ser um inteiro")
    else:
        break

while True: 
    cat = input("Qual a categoria do item entre Lutador, Tank, Suporte, Atirador, Mago e Assassino: ")

    if cat == "Assassino":
        category = "Assassin"
        break
    elif cat == "Mago":
        category = "Mage"
        break
    elif cat == "Atirador":
        category = "ADCarry"
        break
    elif cat == "Suporte":
        category = "Support"
        break
    elif cat == "Tank":
        category = "Tank"
        break
    elif cat == "Lutador":
        category = "Bruiser"
        break
    else:
        input("Categoria invalida, aperta enter pra continuar e vê se digita uma categoria de gente!!")

sql = "INSERT INTO itens (description, value, role) VALUES (%s, %s, %s)"
value = (name, value, category)  

try: 
    cursor.execute(sql, value)
    db.commit()
except:
    input("Algo deu muito errado e o programa explodiu, reabre ele ai!!")
else:
    print("Item inserido com sucesso!!")