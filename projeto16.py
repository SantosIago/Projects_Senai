import os
from time import sleep
os.system("cls")

for num in range(20):#Cria uma variável e um valor que irá determinar quantas vezes vai repitir, e adiciona mais um
 print(num + 1)#Printa o valor da variável mais um, para não iniciar do zero
 sleep(1)
for num in range(20):#Mesma dinâminca 
 print(num + 1, end=" ")#Mesma dinâmica, porém desa vez ele escreverá os valores lado a lado     
 sleep(1)

#Usando while e for para repetição da programação para sempre
# while(True):
#     for num in range(20):
#         print(num + 1)
#         sleep(0.3)
#     for num in range(20):
#         print(num + 1, end=" ")
#         sleep(0.3)
# print()
