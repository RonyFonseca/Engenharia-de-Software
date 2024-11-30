altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

def calcular_imc():
    imc = peso/(altura **2)
    if(imc < 18.5):
        return "Baixo peso"
    elif(imc >= 18.5 and imc <= 24.99):
        return "Normal"
    elif(imc >= 25 and imc <= 29.99):
        return "Sobrepeso"
    else:
        return "Obesidade"

print(calcular_imc())
