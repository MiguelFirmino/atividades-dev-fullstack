## CALCULOS INTERMEDIÁRIOS ##
def obter_subconjuntos(conjunto_inicial):
  # Utilizamos 2 ** N para descobrir a quantidade de subconjuntos
  quantidade_de_subconjuntos = 2 ** len(conjunto_inicial)
  subconjuntos = []

  for i in range(0, quantidade_de_subconjuntos):
    novo_subconjunto = []
    # Maneira fácil de converter um inteiro para binário, usamos [2:] para remover dois algarismos iniciais
    # Queremos iterar o número em binário da direita para a esquerda, por isso, usamos [::-1] para inverte-lo
    index_em_binario = bin(i)[2:][::-1]

    # Tratamos cada algarismo do número binário como "V" ou "F" de uma tabela verdade, sendo que,
    # "V" significa presença de um elemento do conjunto inicial, e "F" significa ausência
    for index, algarismo in enumerate(index_em_binario):
      if algarismo == "1":
        novo_subconjunto.append(conjunto_inicial[index])

    subconjuntos.append(novo_subconjunto)

  return subconjuntos

## ENTRADA DE DADOS ##
# Os elementos do conjunto universo podem ser números ou letras
conjunto_universo = input("Insira os elementos do conjunto universo separados por espaço(' '): ").split(" ")

## APRESENTAÇÃO DOS RESULTADOS ##
print(f'Esses são os possíveis subconjuntos desse conjunto universo: {obter_subconjuntos(conjunto_universo)}')
