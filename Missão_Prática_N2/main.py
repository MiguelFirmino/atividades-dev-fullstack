# Converte um número de qualquer base maior que 0 e menor que 11 para base decimal
def conversao_para_decimal(numero_inicial, base_inicial):
  # devemos inverter o número inicial para que seja feita a soma de cada algarismo
  # vezes a base elevada às suas posições da direita para a esquerda
  numero_inicial = str(numero_inicial)[::-1]
  resultado = 0

  for index, algarismo in enumerate(numero_inicial):
    resultado += int(algarismo) * base_inicial ** index

  return resultado

# Converte um número decimal para qualquer base maior que 0 e menor que 11
def conversao_decimal_para_base(numero_decimal, base):
  resultado = ""

  while numero_decimal >= base:
    numero_decimal, resto = divmod(numero_decimal, base)
    resultado = str(resto) + resultado

  resultado = str(numero_decimal) + resultado

  return int(resultado)

# Converte um número de quaisquer base inicial para uma base final maiores que 0 e menores que 11
def conversao_base_para_base(numero_inicial, base_inicial, base_final):
  # devemos primeiro converter o número inicial para decimal para que depois seja
  # feita a conversão para a base final desejada
  numero_decimal = conversao_para_decimal(numero_inicial, base_inicial)

  resultado = conversao_decimal_para_base(numero_decimal, base_final)

  return resultado

print("Número em base decimal: 100")
print(f"Conversão para base binária: {conversao_decimal_para_base(numero_decimal = 100, base = 2)}")
print(f"Conversão para base octal: {conversao_decimal_para_base(numero_decimal = 100, base = 8)}")
print("")
print("Número em base binária: 1001101")
print(f"Conversão para base decimal: {conversao_para_decimal(1001101, base_inicial = 2)}")
print("")
print("Número em base octal: 152")
print(f"Conversão para base binária: {conversao_base_para_base(numero_inicial = 152, base_inicial = 8, base_final = 2)}")
