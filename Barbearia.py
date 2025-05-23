from time import sleep

# Serviços por profissional
servicos_renan = {
    1: ("Cabelo", 45),
    2: ("Barba", 40),
    3: ("Sobrancelha", 30),
    4: ("Hidratação", 40)
}

servicos_gabriel = {
    1: ("Cabelo", 50),
    2: ("Barba", 45),
    3: ("Sobrancelha", 35),
    4: ("Hidratação", 40)
}

servicos_joel = {
    1: ("Cabelo", 60),
    2: ("Barba", 55),
    3: ("Sobrancelha", 40),
    4: ("Hidratação", 40)
}

print("-" * 10, "Menu Barber shop", "-" * 11)
print("\nEntre no menu: ")
print("1 - Cliente")
print("2 - Profissional Barbeiro")
print("-" * 40)
usuario = int(input("Qual menu deseja entrar? "))
if usuario == 1:
    user = str(input("Qual é seu nome? ")).split()
    sleep(0.5)
    print(f"\nBem-vindo {user[0]}")
    sleep(0.5)
    print("Qual menu deseja prosseguir? \n1 - Agendamento \n2 - Profissionais")
    opcao = int(input(""))
    if opcao == 1:
        print("\nBem-vindo ao agendamento!")
        sleep(0.2)
        # Escolha de profissional
        print("Para começar, com qual profissional você quer agendar?")
        profissional = int(input("Profissional base: 1 \nProfissional Alpha: 2 \nProfissional Premium: 3\n"))
        # Seleciona o conjunto de serviços conforme o barbeiro
        if profissional == 1:
            nome_prof = "Renan"
            servicos = servicos_renan
        elif profissional == 2:
            nome_prof = "Gabriel"
            servicos = servicos_gabriel
        elif profissional == 3:
            nome_prof = "Joel"
            servicos = servicos_joel
        else:
            print("Profissional inválido.")
            exit()
            # Escolha de serviços
        print("\nSelecione os serviços desejados:")
        for codigo, (nome, preco) in servicos.items():
            print(f"{codigo} - {nome} (R${preco:.2f})")

        selecionados = []
        while True:
            servico = input("Digite o número do serviço (ou '0' para finalizar): ")
            if servico == '0':
                break
            if servico.isdigit():
                servico = int(servico)
                if servico in servicos:
                    selecionados.append(servico)
                else:
                    print("Código de serviço inválido.")
            else:
                print("Entrada inválida. Digite apenas números.")
        # Verificar se algum serviço foi selecionado
        if not selecionados:
            print("Nenhum serviço selecionado. Agendamento cancelado.")
        else:
            dia = input("Qual dia deseja marcar? ")
            sleep(0.2)
            mes = input("Qual mês deseja marcar? ")
            sleep(0.2)
            hora = input("Horário: ")
            print("*" * 20)
            print(f"{user[0]}, tudo certo com seu agendamento: \nProfissional {nome_prof}, marcado para o dia {dia}/{mes} às {hora}.")
            print("Favor comparecer 15 minutos antes do seu horário.")
            sleep(0.5)
            print("Serviços selecionados:")
            total = 0
            for codigo in selecionados:
                nome, preco = servicos[codigo]
                print(f"- {nome} (R${preco:.2f})")
                total += preco
            print(f"Total a pagar: R${total:.2f}")
            print("*" * 20)
    elif opcao == 2:
        print("Nossos profissionais são: ")
        print(" 1 - Renan (classe Base) \n cabelo: R$30,00 / barba: R$20,00 / sobrancelha R$15,00 / hidratação: R$25,00")
        print(" 2 - Gabriel (classe Alpha) \n cabelo: R$35,00 / barba: R$25,00 / sobrancelha R$20,00 / hidratação: R$30,00")
        print(" 3 - Joel (classe Premium)  \n cabelo: R$40,00 / barba: R$30,00 / sobrancelha R$25,00 / hidratação: R$35,00")

    else:
        print("Opção inválida")

elif usuario == 2:
    print("Bem vindo, profissional! \nO que deseja fazer hoje? ")
    sleep(0.5)
    print("1 - Calculo de comissão \n ")
    opcao = int(input("Para onde quer seguir? "))
    if opcao == 1:
        print('Calculo de ganho e comissão \n1 - Renan \n2 - Gabriel \n3 - Joel \n0 - Sair')
        while True:
            barbeiro = int(input('Barbeiro: '))
            if barbeiro == 0:
                break
            elif barbeiro == 1:
                corte = 45
                barba = 40
                sobrancelha = 30
                print('Insira a quantidade de servições realizados: ')
                c = int(input('Quantidade de cortes realizados: '))
                sleep(0.5)
                b = int(input('Quantidade de barbas feitas: '))
                sleep(0.5)
                s = int(input('Quantidade de sobrancelhas feitas: '))
                totalc = (corte * c)
                totalb = (barba * b)
                totals = (sobrancelha * s)
                total = (totalc + totalb + totals)
                print(f'Valor total do serviço: R${total}')
            elif barbeiro == 2:
                corte = 50
                barba = 45
                sobrancelha = 35
                print('Insira a quantidade de servições realizados: ')
                c = int(input('Quantidade de cortes realizados: '))
                sleep(0.5)
                b = int(input('Quantidade de barbas feitas: '))
                sleep(0.5)
                s = int(input('Quantidade de sobrancelhas feitas: '))
                totalc = (corte * c)
                totalb = (barba * b)
                totals = (sobrancelha * s)
                total = (totalc + totalb + totals)
                print(f'Valor total do serviço: R${total}')
            elif barbeiro == 3:
                corte = 60
                barba = 55
                sobrancelha = 40
                print('Insira a quantidade de servições realizados: ')
                c = int(input('Quantidade de cortes realizados: '))
                sleep(0.5)
                b = int(input('Quantidade de barbas feitas: '))
                sleep(0.5)
                s = int(input('Quantidade de sobrancelhas feitas: '))
                totalc = (corte * c)
                totalb = (barba * b)
                totals = (sobrancelha * s)
                total = (totalc + totalb + totals)
                print(f'Valor total do serviço: R${total}')
            else:
                print("Barbeiro inexistente em nosso estabelecimento. Tente do 1 ao 3")
    else:
        print("Opção inválida")
        exit()
else:
    print("Opção inválida")