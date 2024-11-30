num = int(input("Digite um número de 0 a 100:"))
i = 0
while (i<30):
    print("")
    i += 1
result = True
while (result==True):
    chute = int(input("Chute um número:"))
    if(chute > num):
        print("Você chutou muito alto !")
    elif(chute < num):
        print("Você chutou baixo")
    elif(chute==num):
        print("Você acertou !")
        result = False
        break