#Projeto tuplas


usuario = (input("Digite seu nome: "),
        input("Digite sua data de nsacimento: "),
        int(input("Digite seu CPF: ")),
        int(input("Digite seu numero de telefone: ")))

print("Seus dados são: ")
print("Nome:", usuario[0])
print("Data de nascimento:", usuario[1])
print("CPF:", usuario[2])
print("Número de telefone:", usuario[3])