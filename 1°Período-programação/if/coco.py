import time
print("""
---------------TIPO DE CLIENTE---------------
[0] - Cliente especial
[1] - Cliente comum
---------------------------------------------
""")
cliente = int(input("Qual o tipo de cliente:"))
qnt_coco = int(input("Quantos cocos foram comprados:"))
time.sleep(1)

if(qnt_coco >= 10):
    valor_coco = qnt_coco * 2
else:
    valor_coco = qnt_coco * 2.50
if(cliente == 0):
    valor_coco = valor_coco - (valor_coco * 0.2)
    print(f"Você é especial 20% de desconto R$:", valor_coco)
else:
    print("Você não é especial R$:", valor_coco)