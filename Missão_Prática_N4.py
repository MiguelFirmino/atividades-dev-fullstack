import numpy as np
import matplotlib.pyplot as plt

# Classe de despesa, armazena informação a respeito dos valores inseridos
# para que sejam inseridos no gráfico
class Despesa:
  def __init__(self, categoria, valores):
    self.categoria = categoria
    self.valores = valores

  # Fórmula da reta da regressão linear conforme x(dias) e y(valores)
  def regressao_linear(self):
    x = range(1, len(self.valores) + 1)
    y = self.valores
    media_x = np.mean(x)
    media_y = np.mean(y)

    erro_x = x - media_x
    erro_y = y - media_y

    soma_erro_xy = np.sum(erro_x * erro_y)
    erro_x_quadratico = erro_x ** 2
    soma_erro_x_quadratico = np.sum(erro_x_quadratico)

    m = soma_erro_xy / soma_erro_x_quadratico
    c = media_y - m * media_x
    reta = m * x + c

    return reta

# Classe de gráfico, serve para controlar a visualização do gráfico plt
class GraficoDespesas:
  def __init__(self):
    pass

  def plotar_despesa(self, despesa):
    dias = np.arange(1, len(despesa.valores) + 1)
    valores_por_dia = np.array(despesa.valores)
    plt.plot(
        dias,
        valores_por_dia,
        marker = "o",
        label = despesa.categoria
        )

  def plotar_regressao(self, despesa):
    plt.plot(
        np.arange(1, len(despesa.valores) + 1),
        despesa.regressao_linear(),
        marker = "o",
        label = f"{despesa.categoria} - Regressão"
    )

  def mostrar(self, titulo):
    plt.legend()
    plt.xlabel("Dia")
    plt.ylabel("Valor em R$")
    plt.title(titulo)
    plt.grid(True)
    plt.show()

# Coleta despesas de acordo com a quantidade de despesas inserida pelo usuário
def coletar_despesas():
  quantidade_de_despesas = int(input("Insira a quantidade de despesas: "))
  quantidade_de_dias = int(input("Insira a quantidade de dias a serem contabilizados: "))

  return [gerar_despesa(quantidade_de_dias) for i in range(0, quantidade_de_despesas)]

# Gera objeto Despesa conforme valores inseridos pelo usuário
def gerar_despesa(quantidade_de_dias):
  nova_despesa = Despesa(
      categoria= input("Insira o nome da categoria de despesa: "),
      valores = [0 for i in range(quantidade_de_dias)]
      )

  # Este bloco obtém os valores do usuário, caso seja inserido "N", todos os
  # valores subsequentes se mantêm 0, como se não houvesse gastos naquele dia
  print("Insira 'N' caso queira parar de registrar os gastos diários")
  dia = 0
  while dia < quantidade_de_dias:
    valor = input(f"Valor gasto em {nova_despesa.categoria} referente ao dia {dia + 1}: ")
    if valor == "N":
      print(f"Valores inseridos {nova_despesa.valores}")
      break
    try:
      nova_despesa.valores[dia] = int(valor)
      dia += 1
    except(ValueError):
      print("ERRO, Insira um valor em número inteiro")
      continue

  return nova_despesa

grafico = GraficoDespesas()
despesas_inseridas = coletar_despesas()

# Plota todas as despesas em um único gráfico
for despesa in despesas_inseridas:
  grafico.plotar_despesa(despesa)
grafico.mostrar(titulo = "Gráfico de Despesas")

# Plota o gráfico de cada despesa e sua regressão linear
for despesa in despesas_inseridas:
  grafico.plotar_despesa(despesa)
  grafico.plotar_regressao(despesa)
  grafico.mostrar(titulo = f"Regressão Linear - {despesa.categoria}")
