altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

imc = peso/(altura **2)
if(imc < 18.5):
    print("Baixo peso")
elif(imc >= 18.5 and imc < 24.99):
    print("Normal")
elif(imc >= 25 and imc < 29.99):
    print("Sobrepeso")
else:
    print("Obesidade")