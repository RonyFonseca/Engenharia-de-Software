i=True
bando_de_dados = []
while i:
    print("=====================")
    print("[0]-[Cadastrar]")
    print("[1]-[Editar]")
    print("[2]-[Modificar]")
    print("=====================")
    res = int(input("Digite o número correspondente a sua opção:"))

    if(res==0):
        nome = input("Digite seu nome:")
        idade = int(input("Me fale sua idade:"))
        cpf = int(input("Digite seu cpf, sem os '.':"))

        def validade(idade):
            if(idade <= 0):
                print("Você não digitou uma idade válida")
                return False
            elif(idade > 0 and idade <=10):
                print("Você é muito novo para se cadastrar nessa plataforma")
                return False
            
        def continuar():
            while True:
                print("===========")
                print("[0]-[Sim]")
                print("[1]-[Não]")
                print("===========")
                cont = int(input("Você deseja continuar na aplicação?:"))
                if(cont==1):
                    break
            
        if(validade(idade)):
            pessoa1 = {"Nome": nome, "Idade": idade, "cpf": cpf}
        else:
            continuar()
        


