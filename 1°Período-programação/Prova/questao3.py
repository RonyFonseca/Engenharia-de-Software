totalAges = []
growsUpsArray = []
amount = 0

while(True):
    try:
        age = int(input("Qual sua idade: "))

        if(age == 0):
            break
        elif(age < 0 or age > 120):
            print("Valor inválido")
            continue
        elif(age <= 18):
            totalAges.append(age)
        else:
            totalAges.append(age)
            growsUpsArray.append(age)
            amount += age
    except:
        print("Apenas valores inteiros são permitidos")

if(len(growsUpsArray) != 0):
    growsUpsArray.sort()
    print(f"a média dos adultos é {amount / len(growsUpsArray)}")
    print(f"A diferença entre o mais velho e o mais novo é: {growsUpsArray[-1] - growsUpsArray[0]}")

print(f"Foram digitadas {len(totalAges)} idades")
