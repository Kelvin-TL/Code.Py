     # Calculadora Py Alterada #
Soma = 1
Subtração = 2
Multiplicação = 3
Divisão = 4
Finalizar_Aplicação = 5
for x in Soma, Subtração, Multiplicação, Divisão, Finalizar_Aplicação:
    print(" Calculadora PY ".center(30,'='))
    print(
    "[1] Soma \n"
    "[2] Subtração \n"
    "[3] Multiplicação \n"
    "[4] Divisão \n"
    "[5] Fechar Aplicação \n"
    )
    Operação = int(input("Digite sua Operação: "))
    print()
    if Operação != 1 and Operação != 2 and Operação != 3 and Operação != 4 and Operação != 5:
        print("Error... :(")
    elif Operação == 1:
       N_1 = int(input("Digite o primeiro número: "))
       N_2 = int(input("Digite o segundo número: "))
       Resultado = N_1 + N_2
       print()
       print(f"O seu resultado é: ",Resultado,"\n")
       pass
    elif Operação == 2:
       N_1 = int(input("Digite o primeiro número: "))
       N_2 = int(input("Digite o segundo número: "))
       Resultado = N_1 - N_2
       print()
       print(f"O seu resultado é: ",Resultado)
       break
    elif Operação == 3:
       N_1 = int(input("Digite o primeiro número: "))
       N_2 = int(input("Digite o segundo número: "))
       Resultado = N_1 * N_2
       print()
       print(f"O seu resultado é: ",Resultado)
       break
    elif Operação == 4:
       N_1 = int(input("Digite o primeiro número: "))
       N_2 = int(input("Digite o segundo número: "))
       Resultado = N_1 / N_2
       print()
       print(f"O seu resultado é: ",Resultado)
       break
    elif Operação == 5:
       print("Finalizando Programa...")
       break

    
