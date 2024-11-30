print(f"""
      -----------------MENU CLIENTES------------------------
      |[0] - Cliente especial
      |[1] - Cliente comum
      ------------------------------------------------------
""")

cliente_type = int(input("Digite o número equivalente ao seu cliente:"))
qnt_cocos = int(input("Quantos cocos comprou:"))
if(cliente_type == 0):
    desconto = 20/100
    if(qnt_cocos >= 10):
        valor_coco = 2
        valor_coco_final = qnt_cocos * valor_coco
        valor_coco_desconto = valor_coco_final - (valor_coco_final * desconto)

    elif(qnt_cocos < 10):
        valor_coco = 2.50
        valor_coco_final = qnt_cocos * valor_coco
        valor_coco_desconto = valor_coco_final - (valor_coco_final * desconto)

    print(f"Você deve pagar R$:{valor_coco_desconto}")
elif(cliente_type == 1):
    if(qnt_cocos >= 10):
        valor_coco = 2
        valor_coco_final = qnt_cocos * valor_coco
    elif(qnt_cocos < 10):
        valor_coco = 2.50
        valor_coco_final = qnt_cocos * valor_coco
    print(f"Você deve pagar R$:{valor_coco_final}")