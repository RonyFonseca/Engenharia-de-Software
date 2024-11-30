# #1
# for i in range(11):
#     print(i)

#2 
# for i in reversed(range(11)):
#     print(i)

#3
# soma = 0
# for num in range(101):
#     soma += num
# print(soma)

#4
# for num in range(51):
#     if(num%2==0):
#         print(num)

#5
# prod = 1
# for i in range(5):
#     i += 1
#     prod = prod * i
# print(prod)

#6
# mult = 0
# for i in range(11):
#     mult = i * 7
#     print(f"{i} x 7 = {mult}")

#7 
# notas_str = input("Digite 5 notas:")
# notas_arr = list(map(int, notas_str.split()))
# qnt_notas = len(notas_arr)
# soma = 0
# for i in range(qnt_notas):
#     soma += notas_arr[i]
# media = soma / qnt_notas
# print("A média é:", media)

#8 
# for i in range(50):
#     i += 1
#     if(i%3 ==0):
#         print(i)

#9 
# nums_str = input("Digite quantos número quiser:")
# nums_arr = list(map(float, nums_str.split()))
# print(f"O maior número digitado foi {max(nums_arr)} e o menor foi {min(nums_arr)}")

#10 
# for i in range(100):
#     i+=1
#     if(i%2!=0):
#         print(i)

#11
# notas_str = input("Digite 5 notas:")
# notas_arr = list(map(int, notas_str.split()))
# qnt_notas = len(notas_arr)
# soma = 0
# for i in range(qnt_notas):
#     if(notas_arr[i] >= 7):
#         soma += 1 

# if(soma > 1):
#     print(soma, " alunos passaram")
# else:
#     print(soma, "aluno passou")

#12 
# numeros = input("Digite um número inteiro:")
# soma = 0
# for i in numeros:
#     soma += int(i)
# print(soma)

#13
# numero = int(input("Digite um número:"))
# for i in range(numero+1):
#     i += 1
#     if(numero % i == 0):
#         print(i)

#14
# alturas_str = input("Digite 5 alturas:")
# alturas_arr = list(map(int, alturas_str.split()))
# qnt_alturas = len(alturas_arr)
# soma = 0
# for i in range(qnt_alturas):
#     soma += =alturas_arr[i]
# media = soma / qnt_alturas
# print("A média é:", media)

#15
# for i in range(101):
#     if(i%3 ==0 and i%5 == 0):
#         i = "FizzBuzz"
#         print(i)
#     elif(i%3 ==0):
#         i = "Fizz"
#         print(i)
#     elif(i%5 == 0):
#         i = "Buzz"
#         print(i)

#16 
# nums = input("Digite os números:")
# soma = 0 
# for i in nums:
#     if(int(i)%2 ==0):
#         soma += int(i)
# print(soma)

#17 
# nums = input("Digite os números:")
# soma = ""
# new_arr = []
# for i in reversed(nums):
#     soma += i
# print(soma)
