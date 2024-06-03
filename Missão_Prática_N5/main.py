from random import randint
import matplotlib.pyplot as plt
from faker import Faker
from wordcloud import WordCloud

class Pessoa:
  def __init__(self, nome, pontuacao):
    self.nome = nome
    self.pontuacao = pontuacao

# GERAR DADOS DE TESTES
def gerar_dados(quantidade_de_pessoas, variacao_pontuacao=10):
  dados = []
  fake = Faker()

  for i in range(quantidade_de_pessoas):
    nome_aleatorio = fake.first_name() # gera primeiro nome
    pontuacao_aleatoria = randint(0, variacao_pontuacao)
    nova_pessoa = Pessoa(nome_aleatorio, pontuacao_aleatoria)
    dados.append(nova_pessoa)

  return dados

# GRAVAR DADOS EM UM ARQUIVO DE TEXTO
def escrever_dados(nome_arquivo, dados):
  try:
    with open(nome_arquivo, "w") as arquivo:
      for pessoa in dados:
        arquivo.write(f"{pessoa.nome} {pessoa.pontuacao}\n")

  except FileNotFoundError:
    print(f"ERRO: Arquivo {nome_arquivo} não encontrado!")

# ABRIR ARQUIVO E LER DADOS
def ler_dados(nome_arquivo):
  dados = []

  try:
    with open(nome_arquivo, "r") as arquivo:
      conteudo = arquivo.readlines()
      for linha in conteudo:
        nome, pontuacao = linha.split()
        nova_pessoa = Pessoa(nome, pontuacao)
        dados.append(nova_pessoa)

      return dados

  except FileNotFoundError:
    print(f"ERRO: Arquivo {nome_arquivo} não encontrado!")

# MANIPULAÇÃO DOS DADOS
def gerar_probabilidades(dados):
  pontuacoes = {}

  # registra a quantidade de ocorrências de cada valor
  for pessoa in dados:
    pontuacao = int(pessoa.pontuacao)
    if pontuacao in pontuacoes:
      pontuacoes[pontuacao] += 1
    else:
      pontuacoes[pontuacao] = 1

  # registra a probabilidade de ocorrência de cada valor
  total = len(pontuacoes)
  for pontuacao, ocorrencia in pontuacoes.items():
    pontuacoes[pontuacao] = ocorrencia / total

  return pontuacoes

# VISUALIZAÇÃO DAS PROBABILIDADES EM HISTOGRAMA
def plotar_histograma(probabilidades):
  plt.title("Histograma")
  plt.xlabel("Pontuações")
  plt.ylabel("Probabilidade")
  plt.xlim(-1, 11)
  plt.grid()
  plt.bar(probabilidades.keys(),
          probabilidades.values(),
          width=0.9)

  plt.show()

# TODO: MANIPULAR DADOS PARA VISUALIZÁ-LOS EM UMA NUVEM DE PALAVRAS
def plotar_nuvem(probabilidades):
  palavras = {0 : "zero", 1 : "um", 2 : "dois",
              3 : "três", 4 : "quatro", 5 : "cinco",
              6 : "seis", 7 : "sete", 8 : "oito",
              9 : "nove", 10 : "dez"}
  traducao = list(map(lambda x: palavras[x], probabilidades))
  texto = " ".join(traducao)

  nuvem = WordCloud(background_color="black",
                    min_font_size=10,
                    width=500,
                    height=300,
                    )
  nuvem.generate(texto)
  plt.figure(figsize=(8, 8), facecolor=None)
  plt.imshow(nuvem)
  plt.axis("off")
  plt.tight_layout(pad=0)
  plt.show()

# GERAÇÃO DE DADOS ALEATÓRIOS COM BASE EM QUANTIDADE
# DE PESSOAS E VARIAÇÃO DE SUAS PONTUAÇÕES
pessoas = gerar_dados(quantidade_de_pessoas=10)

# ESCRITA E LEITURA DE DADOS NO ARQUIVO DE TEXTO
# OBSERVAÇÃO: A VARIÁVEL "PESSOAS" E "DADOS" SÃO
# EQUIVALENTES, JÁ QUE A FUNÇÃO "ler_dados" RETORNA
# UMA LISTA DE OBJETOS DO TIPO PESSOA DA MESMA
# FORMA QUE A FUNÇÃO "escrever_dados" AS GERAM
escrever_dados("dados.txt", pessoas)
dados = ler_dados("dados.txt")

# MANIPULAÇÃO DOS DADOS PARA VISUALIZAÇÃO
probabilidades = gerar_probabilidades(dados)

# VISUALIZAÇÃO DAS PROBABILIDADES
plotar_histograma(probabilidades)

# VISUALIZAÇÃO DA NUVEM DE PALAVARAS
plotar_nuvem(probabilidades)