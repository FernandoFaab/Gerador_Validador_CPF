while True:

    resposta = int(input('Você deseja gerar ou validar um CPF? (GERAR=1 - VALIDAR=2): '))

    if resposta == 1:
        cpf = input('Digite os nove primeiros números: ')
        cpf_list = list(map(int, cpf))

        soma1 = 0
        i = 10
        for valor in cpf_list:
            soma1 = soma1 + valor * i
            i = i - 1

        soma1 = (11 - (soma1 % 11))

        cpf_list.append(soma1)

        soma2 = 0
        i = 11
        for valor in cpf_list:
            soma2 = soma2 + valor * i
            i = i - 1
        soma2 = (11 - (soma2 % 11))

        cpf_list.append(soma2)

        print(*cpf_list, sep='')

    else:
        cpf = input('Digite um CPF: ')
        cpf_list = list(map(int, cpf))

        digito1 = cpf_list[9]
        digito2 = cpf_list[10]

        del (cpf_list[9:])

        soma1 = 0
        i = 10
        for valor in cpf_list:
            soma1 = soma1 + valor * i
            i = i - 1

        soma1 = (11 - (soma1 % 11))

        if soma1 == digito1:
            cpf_list.append(soma1)
            soma2 = 0
            i = 11
            for valor in cpf_list:
                soma2 = soma2 + valor * i
                i = i - 1
            soma2 = (11 - (soma2 % 11))
            if soma2 == digito2:
                print("CPF válido")
            else:
                print("CPF inválido")
        else:
            print("CPF inválido")