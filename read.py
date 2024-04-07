import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='leoncioStore'
)

cursor = db.cursor()

while True:
    try:
        option = int(input("Digite 1 para o relatório geral e 2 para uma busca especifica: "))
    except:
        print("A opção deve ser um inteiro.")
        input("Aperta ENTER para digitar novamente")
    else:
        if option not in [1,2]:
            print("Opção invalidade!!")
            input("Aperte ENTER para digitar novamente")
        else:
            break

if option == 1 :
    cursor.execute("SELECT * FROM itens")

    result = cursor.fetchall()

    for i in result:
        print(i)
elif option == 2:
    search = input("Digite a palavra chave a ser buscada: ")
    value = (search, )

    cursor.execute("SELECT * FROM itens WHERE description = %s", value)

    # if cursor.rowcount < 1 :
    #     print("Nenhum resultado encontrado!!")
    #     input("Aperte ENTER para continuar")
    # else :
    result = cursor.fetchall()

    for i in result :
        print(i)