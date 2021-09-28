#python 3.7

print ("################################")
print ("#1- ADICAO -> +                #")
print ("#2- SUBTRACAO -> -             #")
print ("#3- DIVISAO -> /               #")
print ("#4- MULTIPLICACAO -> x         #")
print ("#5- SAIR -> 5                  #")
print ("################################")

escolha = input("ESCOLHA QUAL TIPO DE CONTA DESEJAS FAZER: ")

if escolha == 1:
    x = input("DIGITE O PRIMEIRO NUMERO A SER CALCULADO: ")
    y = input("DIGITE O SEGUNDO NUMERO A SER CALCULADO: ")
    RESULT = x + y
    print ("RESULTADO: ") + str(RESULT)
elif escolha == 2:
    x = input("DIGITE O PRIMEIRO NUMERO A SER CALCULADO: ")
    y = input("DIGITE O SEGUNDO NUMERO A SER CALCULADO: ")
    RESULT = x - y
    print ("RESULTADO: ") + str(RESULT)
elif escolha == 3:
    x = input("DIGITE O PRIMEIRO NUMERO A SER CALCULADO: ")
    y = input("DIGITE O SEGUNDO NUMERO A SER CALCULADO: ")
    RESULT = x / y
    print ("RESULTADO: ") + str(RESULT)
elif escolha == 4:
    x = input("DIGITE O PRIMEIRO NUMERO A SER CALCULADO: ")
    y = input("DIGITE O SEGUNDO NUMERO A SER CALCULADO: ")
    RESULT = x * y
    print ("RESULTADO: ") + str(RESULT)
elif escolha == 5:
    print ("FECHANDO A CALCULADORA...")
