"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# código
while True:
    cpf = input('Digite um CPF: ')
    cpf_list = list(map(int, cpf))

    digito1 = cpf_list[9]
    digito2 = cpf_list[10]

    del(cpf_list[9:])

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






