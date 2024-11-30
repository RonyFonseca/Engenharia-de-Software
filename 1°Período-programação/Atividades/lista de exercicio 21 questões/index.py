#1
#A diferença começa na sintaxe onde o for faz seu própio incremento enquanto o while não 
#o while ele fica executando enquanto a condição atribuida a ele for verdadeira
#for ele ja vem com um incremento própio é usado quando temos uma quantidade de repetição especifica

#2
#Iremos usar o for quando soubermos a quantidade de repetições que queremos que ele execute
#já o while usamos quando não sabemos quantas vezes queremos executar alguma estrutura

#3
# i = 1
# while (i!=11):
#     print(i)
#     i += 1

#4
# i = 10
# while (i!=0):
#     print(i)
#     i -= 1

#5
# soma = 0
# i = 1
# while (i!=101):
#     soma += i
#     i+=1
# print(soma)

#6 
# mult = 1 
# i = 1
# while(i!=6):
#     mult *= i 
#     i+= 1
# print(mult)

#7 
# i = 1
# while(i!=11):
#     print(f"9 X {i} = { 9* i}")
#     i+=1

#8 
# arr = []
# n = 1
# while (n!=0):
#     n = int(input("Digite um número:"))
#     if(n != 0):
#         arr.append(n)
# print("O maior número digitado foi:", max(arr))
# print("O menor número digitado foi:", min(arr))

#9
# arr = []
# i = 0
# media = 0
# while(i!=-1):
#     i = int(input("Digite um valor:"))
#     if(i != -1):
#         arr.append(i)
# media = (sum(map(int, arr))) / len(arr)
# print("A média é:",media)

#10 
# numStr = input("Digite um número inteiro:")
# i = 0
# soma = 0
# while(i!=len(numStr)):
#     print(f"{numStr[i]}^3 = {int(numStr[i])**3}")
#     soma += int(numStr[i])**3
#     i+=1
# print("=====================")
# print("A soma deles é:",soma)
# print("=====================")

#11
# i = 1
# impar = []
# while(i!=101):
#     if(i%2!=0):
#         impar.append(i)
#     i+=1
# print(impar)

#12
# i = 0
# multiplos = []
# while(i!=51):
#     if(i%3==0):
#         multiplos.append(i)
#     i+=1
# print(multiplos)
        
#13
# nota = input("Digite todas notas separadas por espaço:")
# notas = list(map(float, nota.split()))

# i = 0
# alguem_passou = True
# while(i!= len(notas)):
#     if(notas[i] >= 7):
#         print(f"O {i+1}° aluno foi aprovado")
#         alguem_passou = False
#     i+=1
# if(alguem_passou):
#     print("Nem uma alma penada passou!")

#14
# par = []
# impar = False
# impar_num = []
# n = 1
# while(n!=0):
#     n = int(input("Digite um número"))
#     if(n%2==0):
#         if(impar):
#             continue
#         else:
#             par.append(n)  
#     else:
#         impar = True  
#         impar_num.append(n)
        
# print(f"Os pares digitados antes do impar {impar_num[0]} são: {par}")


#15
# par = 0
# impar = 0
# num = 1
# while (num!=0):
#     num = int(input("Digite um numero:"))
#     if(num%2==0):
#         par+=1
#     else:
#         impar+=1
# print(f"Par: {par}")
# print(f"Impar: {impar}")

#16
# d2_d5 = 0
# d2_d3 = 0
# d2 = 0
# d3 = 0
# d5 = 0
# numeros = []
# num = 1
# while (num!=0):
#     num = int(input("Digite um numero:"))
#     numeros.append(num)
#     if(num%2==0 and num%5==0):
#         d2_d5+=1
#     if(num%2==0 and num%3==0):
#         d2_d3+=1
#     elif(num%2 ==0):
#         d2+=1
#     elif(num%3 ==0):
#         d3+=1
#     elif(num%5 ==0):
#         d5+=1
# print("===============================")
# print(numeros)
# print("===============================")
# print(f"Divisíveis só por 2: {d2}")
# print(f"Divisíveis só por 3: {d3}")
# print(f"Divisíveis só por 5: {d5}")
# print(f"Divisíveis por 2 e 3: {d2_d3}")
# print(f"Divisíveis por 2 e 5: {d2_d5}")

#17 
# num = 1 
# numeros = []
# media = 0
# while(num!=0):
#     num = int(input("Digite um número:"))
#     if(num!=0):
#         if(num%3==0):
#             numeros.append(num)
# print(numeros,"/", len(numeros))
# print(f"A média é {(sum(map(float, numeros)))/ len(numeros)}")

#18
# num = 0 
# mais_3 = 0
# while(num!="0"):
#     num = input("Digite um número")
#     if(len(num)>3):
#         mais_3 += 1
# print("Mais de 3 digitos quantidade:",mais_3)        

#19
# num = 1
# media = 0
# soma = 0
# qnt = 0
# while(num!=0):
#     num = int(input("Digite valores:"))
#     if(num>=50 and num<=100):
#         soma+=num
#         qnt+=1
# print(f"A media é: {soma/qnt}")

#20
# num = 1
# numeros = []
# while(num!=0):
#     num = int(input("Digite valores:"))
#     if(num%2!=0 and (num%2!=0)>0):
#         numeros.append(num)
# print(f"O menor valor digitado é {min(numeros)}")

#21
# n = 1
# impar = 0 
# par = 0 
# while(n!=0):
#     n = int(input("Digite um valor"))
#     if(n!=0):
#         if(n%2==0):
#             par+=1
#         else:
#             impar+=1
# print("Par:",par)
# print("Impar:",impar)
        