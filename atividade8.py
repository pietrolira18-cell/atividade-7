

usuario_correto = "admin"
senha_correta = "1234"

while True:

    usuario = input("usuario: ")
    senha = input("senha: ")

    if usuario == usuario_correto:

        if senha == senha_correta:
            print("login feito")
            break

        else:
            print("senha errada")

    else:
        print("usuario errado")




print("\nMERCADO\n")

print("1 - arroz = 25")
print("2 - feijao = 10")
print("3 - macarrao = 8")
print("4 - refrigerante = 12")
print("5 - carne = 40")

total = 0

while True:

    p = int(input("\nescolha o produto: "))

    if p == 1:
        nome = "arroz"
        valor = 25

    elif p == 2:
        nome = "feijao"
        valor = 10

    elif p == 3:
        nome = "macarrao"
        valor = 8

    elif p == 4:
        nome = "refrigerante"
        valor = 12

    elif p == 5:
        nome = "carne"
        valor = 40

    else:
        print("produto invalido")
        continue

    qtd = int(input("quantidade: "))

    soma = valor * qtd
    total = total + soma

    print("produto:", nome)
    print("subtotal:", soma)

    continuar = input("quer continuar? (S/N): ").upper()

    if continuar != "S":
        break



print("\nTOTAL:", total)

print("\n1 - dinheiro")
print("2 - cartao")
print("3 - pix")

pg = int(input("pagamento: "))

if pg == 1:

    desc = total * 0.10
    final = total - desc
    print("desconto:", desc)

elif pg == 2:

    final = total





elif pg == 3:

    desc = total * 0.05
    final = total - desc
    print("desconto:", desc)

else:

    final = total
    print("opcao invalida")



print("\nVALOR FINAL:", final)
print("volte sempre")
