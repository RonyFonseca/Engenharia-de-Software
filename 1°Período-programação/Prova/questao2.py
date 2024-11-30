oldPrice = float(input("Qual o preço antigo: "))

if(oldPrice <= 50):
    risePercentage = 0.05
elif(oldPrice <= 100):
    risePercentage = 0.1
else:
    risePercentage = 0.15

newPrice = oldPrice * (1+risePercentage)

if(newPrice <= 80):
    print("Barato")
elif(newPrice <= 120):
    print("Normal")
elif(newPrice <= 200):
    print("Caro")
else:
    print("Muito caro")