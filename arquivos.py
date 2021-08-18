from db_list import lista

# file = open('file.txt', 'a')

# texto = input('O que deseja adicionar: ')
# num = 1
# print('\n')
# file.write(str(num) + '\n' + texto)
# file.close()
# file = open('file.txt', 'r')

for i in range(16, len(lista)):
    print(lista[i])

# r leitura
# w Escrita, substitui o conteudo do arqui existente
# x Escrita retorna um erro caso o arquivo ja exista
# a Escrita , insere novos dados no final do arqu
# b modo bin
# t modo texto ..padrao
# + atualizar tanto leitura quanto escrita