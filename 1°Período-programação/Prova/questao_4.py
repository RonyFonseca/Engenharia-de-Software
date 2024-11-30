valor_do_cliente = float(input("Qual foi o valor gasto:"))
desconto = 10/100
valor_10_de_desconto = valor_do_cliente - (valor_do_cliente * desconto)
valor_restado_para_o_vendedor_se_descontado = valor_10_de_desconto*(5/100)

valor_3_parcelas = valor_do_cliente / 3
valor_restado_para_o_vendedor_se_parcelado = valor_do_cliente*(5/100)

print(f"O cliente vai pagar R$:{valor_10_de_desconto} com 10% de desconto")
print(f"E o valor parcelado em 3x sem juros fica R$:{valor_3_parcelas:.2f}")
print(f"A comisão do vendedor, no caso da venda ser a vista é de R$:{valor_restado_para_o_vendedor_se_descontado:.2f}")
print(f"A comisão do vendedor, no caso da venda parcelada é de R$:{valor_restado_para_o_vendedor_se_parcelado:.2f}")
