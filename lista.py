# lista.sort() Ordenacao em ordem
# lista.sort(reverse=True) Odenacao em ordem inversa
# list.append(valor) Insert valor na lista
# print(f'{}')
# lista.pop() Deleta o ultimo elemento da lista

# for l in lista:
#     print(f'{l}')
#     time.sleep(1)
import time

nome = input('Qual seu nome? ')
print(f'Ola {nome}! prazer em te-lo aqui..')
time.sleep(2)
data_nasc = input(f'{nome} Qual o dia do seu nascimento ?')
mes_nasc = input(f'{nome} Qual o mês do seu nascimento ? ')
ano_nas = input(f'{nome} Qual o ano do seu nascimento ? ')

print(' ')

print(f'{nome} Voçe nasceu em {data_nasc} {mes_nasc} {ano_nas}')
