print("\033[35m=-" * 20)
print("BEM-VINDO(A) A CALCULADORA DE MÉDIA")
print("=-" * 20, "\033[m")

nota_final = 0

for num in range(10):
    num += 1
    print("\033[36mNota", num, ":")
    nota = float(input("Digite o valor da nota:"))
    nota_final = nota + nota_final
print("A média de tudo é de:", nota_final / 10)