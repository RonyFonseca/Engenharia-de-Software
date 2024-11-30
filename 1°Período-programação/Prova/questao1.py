height = float(input("QUal sua altura: "))
weight = float(input("Qual o seu peso: "))

if(height < 1.2):
    posibilitiesHeight = ["A", "D", "G"]
elif(height >= 1.2 and height < 1.7):
    posibilitiesHeight = ["B", "E", "H"]
else:
    posibilitiesHeight = ["C", "F", "I"]

if(weight < 60):
    posibilitiesWeight = ["A", "B", "C"]
elif(weight >= 60 and weight <= 90):
    posibilitiesWeight = ["D", "E", "F"]
else:
    posibilitiesWeight = ["G", "H", "I"]

for pH in posibilitiesHeight:
    for pW in posibilitiesWeight:
        if(pH == pW):
            print(f"Sua classificação é: {pW}")