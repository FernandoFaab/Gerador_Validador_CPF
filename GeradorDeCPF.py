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

print(*cpf_list, sep= '')

