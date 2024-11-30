lotes = 142
representantes = 18 
fracao = 4/100

fracao_aglomerada_das_pessoas = fracao * 18
calculo_de_terra_por_pessoa = (142 - (fracao_aglomerada_das_pessoas * lotes))/18
calculo_de_sobra_da_terra = 142 - (calculo_de_terra_por_pessoa * 18)

print(f"Cada pessoa vai receber {calculo_de_terra_por_pessoa:.2f} lotes")
print(f"Sobrou {calculo_de_sobra_da_terra} lotes para prefeitura")
