# numero = int(input("Digite um número qualquer:"))
# if(numero > 0):
#     print("Seu número é positivo")
# elif(numero == 0):
#     print("Seu número é igual a zero")
# else:
#     print("Seu número é negativo")


# idade = int(input("Digite sua idade:"))
# if (idade > 20):
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")


# num = input("Digite dois números:")
# num_arr = num.split()
# print(f"O número maior digitado foi {max(num_arr)}")


# num = int(input("Digite um número inteiro:"))
# if(num%2 == 0):
#     print("É par")
# else:
#     print("É impar")



# nums = input("Digite três notas:")
# nums_arr = nums.split()
# print(nums_arr)
# media = (float(nums_arr[0]) + float(nums_arr[1]) +
#          float(nums_arr[2]))  / 3
# print(media)
# if(media >= 7):
#     print("Aprovado")
# else:
#     print("Reprovado")


# nomes = input("Digite dois nomes:")
# nomes_arr = nomes.split()
# print(max(nomes_arr))

# caracter = input("Digite uma letra:")
# vogais = ["a", "e", "i", "o", "u"]
# if(caracter.lower() in vogais):
#     print("É uma vogal")
# else:
#     print("É uma consoante")



# num = input("Digite os número:")
# num_arr = num.split()
# new_nums = sorted(num_arr)

# for num in new_nums:
#     print(num)





# peso = float(input("Digite seu peso:"))
# altura = float(input("Digite sua altura:"))
# imc = peso/altura**2
# if(imc<18.5):
#     print("Baixo peso")
# elif(imc >= 18.6 and imc<=24.9):
#     print("Peso normal")
# elif(imc >= 25 and imc<=29.9):
#     print("Sobrepeso")
# elif(imc >= 30 and imc<=34.9):
#     print("Obesidade grau I")
# elif(imc >= 35 and imc<=39.9):
#     print("Obesidade grau II")
# else:
#     print("Obesidade grau III")



# num1 = int(input("Qual o número:"))
# meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# print(f"seu mês é {meses[num1-1]}")


# salario = float(input("De quanto é seu salário:"))
# if(salario > 1500):
#     aumento_fracao = 10/100
#     aumento = float(aumento_fracao) * salario
#     new_salario = salario + aumento
#     print(f"Seu aumento foi de R$: {aumento}, seu salário ficou {new_salario}")
# else:
#     aumento_fracao = 15/100
#     aumento = aumento_fracao * salario
#     new_salario = aumento + salario
#     print(f"Seu aumento foi de R$: {aumento}, seu salário ficou {new_salario}")



# num = int(input("Digite um número inteiro: "))
# if((num%3 == 0) and (num%5 == 0)):
#     print("É divisivel")
# else:
#     print("Não é divisivel")


# dia_user = input("Digite um dia da semana: ")
# dia_user_tratado = dia_user.lower()

# dia_util = ["segunda", "terça", "quarta", "quinta", "sexta"]

# if(dia_user_tratado in dia_util):
#     print("É um dia útil")
# else:
#     print("Fim de semana")




# import time
# num = int(input("Digite um número de 1 a 5: "))
# if(num > 5):
#     print("------------- O número tem que ser só de 1 a 5 -----------------")
# else:
#     time.sleep(1)
#     if(num == 1):
#         print("Muito Bom")
#     elif(num == 2):
#         print("Bom")
#     elif(num == 3 ):
#         print("Insuficiente")
#     else:
#         print("Muito Insuficiente")




# dia_num = int(input("Digite um número: "))
# semana = ["domingo","segunda", "terça", "quarta", "quinta", "sexta", "sábado"]
# print(f"O dia da semana que corresponde ao seu número é {semana[dia_num-1]}")





# try:
#     num = float(input("Digite um número: "))
#     arrendondar = round(num)
#     print(arrendondar)
# except:
#     print("Deu erro")





# idade = int(input("Digite sua idade: "))
# if(idade >= 0 and idade <=1):
#     print("Bebê")
# elif(idade>=1 and idade <=12):
#     print("Criança")
# elif(idade>=13 and idade <=18):
#     print("Adolescente")
# else:
#     print("Adulto")




# num = input("Digite dois números: ")
# num_arr = num.split()
# print(f"======================================")
# print(f"[1] - Somar")
# print(f"[2] - Subtrair")
# print(f"[3] - Multiplicar")
# print(f"[4] - Dividir")
# print(f"======================================")
# opc = int(input("Digite a opção que vc quer: "))
# if(opc == 1):
#     result = int(num_arr[0]) + int(num_arr[1])
# elif(opc == 2):
#     result = int(num_arr[0]) - int(num_arr[1])
# elif(opc == 3):
#     result = int(num_arr[0]) * int(num_arr[1])
# elif(opc == 4):
#     result = int(num_arr[0]) / int(num_arr[1])
# print(result)




# try:
#     nome = input("Digite seu nome: ")
#     idade = int(input("Digite sua idade: "))
#     print(f"Olá {nome}, como posso ajudar?")
#     user = input(":")
# except ValueError:
#     print("O valor digitado tem quer ser inteiro")




# try:
#     metro = float(input("Digite o valor em metro: "))
#     centimetro = metro * 100
#     milimetro = metro * 1000
#     km = metro * 0.001
#     print(f"Centimetros: {centimetro}")
#     print(f"Milimetros: {milimetro}")
#     print(f"Km: {km}")
# except:
#     print("Deu erro em algo")