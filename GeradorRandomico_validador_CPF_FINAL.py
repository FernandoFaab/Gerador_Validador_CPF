while True:

    resposta = int(input('Você deseja gerar ou validar um CPF? (GERAR=1 / VALIDAR=2 / ENCERRAR=3): '))

    while True:
        if resposta == 1:
            cpf_list = []
            import random
            for x in range(0, 9):
                cpf = random.randint(0, 9)
                cpf_list.append(cpf)

            soma1 = 0
            i = 10
            for valor in cpf_list:
                soma1 = soma1 + valor * i
                i = i - 1
            soma1 = (11 - (soma1 % 11))
            if soma1 > 9:
                soma1 = 0

            cpf_list.append(soma1)

            soma2 = 0
            i = 11
            for valor in cpf_list:
                soma2 = soma2 + valor * i
                i = i - 1
            soma2 = (11 - (soma2 % 11))
            if soma2 > 9:
                soma2 = 0

            cpf_list.append(soma2)

            print(*cpf_list, sep='')
            break

        if resposta == 2:
            cpf = input('Digite um CPF: ')

            if cpf.isdigit():

                digitos = len(str(cpf))
                if digitos == 11:

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
                    if soma1 > 9:
                        soma1 = 0

                    if soma1 == digito1:
                        cpf_list.append(soma1)
                        soma2 = 0
                        i = 11
                        for valor in cpf_list:
                            soma2 = soma2 + valor * i
                            i = i - 1
                        soma2 = (11 - (soma2 % 11))
                        if soma2 > 9:
                            soma2 = 0

                        if soma2 == digito2:
                            print("CPF válido")
                            break
                        else:
                            print("CPF inválido")
                            break
                    else:
                        print("CPF inválido")
                else:
                    print('Você deve digitar um cpf contendo 11 números!')
                    continue
            else:
                print('Você só pode digitar números!')
                continue
        if resposta == 3:
            exit()
        else:
            print('Digite uma opção válida!')
            break
