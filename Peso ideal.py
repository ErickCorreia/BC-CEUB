altura = float(input("Altura (m): "))
sexo = input("Sexo (M/F): ").strip().upper()

if sexo == "M":
    print(f"Peso ideal: {(72.7 * altura - 58):.2f} kg")
elif sexo == "F":
    print(f"Peso ideal: {(62.1 * altura - 44.7):.2f} kg")
else:
    print("Sexo inválido!")