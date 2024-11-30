# 1
# num = input("Digite um número: ")
# print("Seu número foi:", num)
# print("O tipo dele é", type(num))


# 2
# num1 = input("Digite o número 1:")
# num2 = input("Digite o número 2:")
# soma = int(num1)+int(num2)
# print("A soma de ", num1, "+", num2, "=", soma )


# 3
# print("Rony" + "Fonseca")
# str1 = "Rony"
# str2 = "Fonseca"
# print(str1+str2)


# 4
# nome = input("Qual é seu nome:")
# print("Bem vindo,",nome)


# 5
# idade = input("Qual sua idade:")
# conversao = int(idade)
# print("Sua idade em Int é", conversao)


# 6
# num = int(input("Digite um número inteiro:"))
# conversao = float(num)
# print("Seu número em float é,",conversao)


# 7
# num1 = input("Digite o número 1:")
# num2 = input("Digite o número 2:")
# soma = int(num1)+int(num2)
# print("A soma de ", num1, "+", num2, "=", soma )


# 8
# num = float(input("Digite um número:"))
# calculo = num**2
# print("O quadrado do número", num, "é", calculo)



# 9 
# idade_nascimento = int(input("Digite seu ano de nascimento:"))
# calculo = 2024 - idade_nascimento
# print("Sua idade é",calculo)


# 10 
# nome = input("Digite seu nome:")
# sobrenome = input("Digite seu sobrenome:")
# print("Olá", nome + sobrenome)


# 11
# numeros = input("Digite números:")
# new_numbers = numeros.split()
# print("Quantidade de número é ",len(new_numbers))


# 12
# animal = input("Digite um animal:")
# print("Seu animal é:", animal)


# 13 
# nome = input("Qual é seu nome:")
# sobrenome = input("Qual seu sobre nome:")
# print(sobrenome+nome)


# 14 
# str = input("Digite alguma coisa:")
# print(len(str))


# 15 
# num = int(input("Digite um número:"))
# if((num%2)==0):
#     print("Par")
# else:
#     print("Impar")


# 16 
# num = float(input("Digite um  número:"))
# if(num<0):
#     print("É negativo")
# else: 
#     print("Positivo")


# 17 
# numeros = input("Digite dois números:")
# condicao = numeros.split()
# print("Maior valor é:", max(condicao))


# 18 
# altura = float(input("Digite sua altura:"))
# peso = float(input("Digite seu peso:"))
# imc = peso/altura**2 
# print("O imc é:", imc)


# 19
# nome = input("Digite seu nomer:")
# if(len(nome)> 5):
#     print("Seu nome é maior que 5 caracteres")
# else:
#     print("Seu nome é menor que 5 caracteres")


# 20 
# estado = input("Seu estado civil:")
# if(estado=="Casado"):
#     print("Você é casado")
# elif(estado=="Solteiro"):
#     print("Você ta solteiro")
# else:
#     print("Você está em algo não indentificado")


# 21 
# base = float(input("Digite a base do triângulo:"))
# altura = float(input("Digite a baltura do triângulo:"))
# calc = base*altura/2
# print("A área dele é", calc)


# 22
# cidade = input("Digite sua cidade:")
# if(cidade[0]=="J"):
#     print("Sua cidade começa com J")
# else:
# print(TypeError())


# 23
# nums = input("Digite dois números:")
# num = nums.split()
# print("A soma de", num[0], "+", num[1], "é", int(num[0]) + int(num[1]))


# 24 
# num = float(input("Digite um número decimal:"))
# convert = int(num)
# print(type(convert))


# 25
# num = input("Digite um número:")
# num_int = int(num) + 10
# num_str = str(num_int)
# print(type(num_str))


# 26 
# data_nao_formatada = input("Digite a data de hoje xx/xx/xx :")
# data_formatada = data_nao_formatada.split("/")
# dia = int(data_formatada[0])
# mes = int(data_formatada[1])
# ano = int(data_formatada[2])
# print("=============================================================")
# print("O usuário digitou o dia", dia, "do mês", mes, "de", ano)
# print("=============================================================")
# print("o tipo de dia:", type(dia))
# print("o tipo de mes:", type(mes))
# print("o tipo de ano:", type(ano))
# print("=============================================================")


# 27
# cidade = input("Qual o nome da sua cidade:")
# estado_unico_da_faculdade = "PE"
# print("Você mora em", cidade, estado_unico_da_faculdade)


# 28
# ano_nascimento = int(input("Digite seu ano de nascimento:"))
# print("Bem-vindo ao nosso programa, nascido em", ano_nascimento)


# 29 
# num = int(input("Digite um número:"))
# palavra = input("Digite uma palavra:")
# num_str = str(num) + " " + palavra
# print(num_str, type(num_str))


# 30 
# preco_escova_de_dente = 2.50 
# preco_sabonete = 5
# preco_da_agua_1L = 2.50
# print("""
# ==================================
# [1] - escova de dente
# [2] - 1L de água
# [3] - sabonete
# ==================================
# """)
# produto = int(input("Digite o número de um produto:"))
# if(produto == 1):
#     print("===============================================================")
#     print("[Escova de dente está custando R$:",preco_escova_de_dente,"]")
#     print("===============================================================")
# elif(produto == 2):
#     print("============[1L está custando R$:",preco_da_agua_1L,"]============")
#     litro_de_agua_do_cliente = int(input("Você vai querer quantos litros de água:"))
#     print("===============================================================")
#     calculo_da_agua = preco_da_agua_1L * litro_de_agua_do_cliente
#     print("[Valor a ser pago R$:",calculo_da_agua,"]")
# elif(produto == 3):
#     print("===============================================================")
#     print("[Escova de dente está custando R$:",preco_sabonete,"]")
#     print("===============================================================")
# else:
#     print("Você não selecionou nem uma das opções apresentadas no menu")


# 31
# num_user = int(input("Digite um número:"))
# num_user_quadrado = num_user**2
# print("O quadrado de ", num_user, "é", num_user_quadrado)


# 32 
# email = input("Digite seu E-mail:")
# print(len(email))
# if(len(email)> 15):
#     num_de_iguais = 50
# if(len(email)<=15):
#     num_de_iguais = 40
# print("="*num_de_iguais)
# print(f"        Bem vindo {email}       ")
# print("="*num_de_iguais)


# 33 
# num = input("Digite dos números separados por espaço:")
# num_formatado_array = num.split()
# num1 = int(num_formatado_array[0])
# num2 = int(num_formatado_array[1])
# soma = num1 + num2
# multiplicacao = num1 * num2
# divisao = num1 / num2
# print(f"soma:{soma}, Multiplicação:{multiplicacao}, Divisão:{divisao}")


# 34 
# base = float(input("Digite a base do triângulo:"))
# altura = float(input("Digite a baltura do triângulo:"))
# calc = base*altura/2
# print("A área dele é", calc)


# 35
# raio = float(input("Digite o raio da circunferência:"))
# PI = 3.14
# calc = 2*PI*raio
# print("Raio:", calc)


# 36
# base = float(input("Digite a base do triângulo:"))
# altura = float(input("Digite a baltura do triângulo:"))
# calc = base*2 + altura*2
# print("O perímetro dele é", calc)


# 37 
# num = input("Digite três números decimais separados por espaço:")
# num = num.split()
# num1 = float(num[0])
# num2 = float(num[1])
# num3 = float(num[2])
# media = (num1 + num2 + num3)/ len(num)
# print("A média é:",media)


# 38 
# idade = int(input("Quantos anos você tem?:"))
# dias = idade*365
# mes = dias/30
# print("Você está vivo:", dias,"dias")
# print(f"Você está vivo:{mes:.0f}")


# 39 
# reais = float(input("Valor em Reais R$:"))
# dolar = float(input("Qual o valor do dolar atual:"))
# calc = reais*dolar
# print(f"O valor em dolar é:{calc:.2f}")


# 40 
# num= float(input("Digite um número decimal:"))
# conversao = round(num)
# print("Arredondado:",conversao)


# 41 
# num = input("Digite três números separados por espaço:")
# num = num.split()
# num1 = int(num[0])
# num2 = int(num[1])
# num3 = int(num[2])
# calc = (num1 + num2)*num3
# print("A média é:",calc)


# 42 
# grau_C = float(input("Digite uma temperatura em Celsius C°:"))
# grau_F = (grau_C * (9/5))+32
# print("Seu grau em Fahrenheit é F°:", grau_F)