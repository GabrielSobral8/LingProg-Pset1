def main():
  nmrCartao = input("Insira o número do cartão de crédito: ")
#funcao para informar se é valido ou nao o numero do cartao após passar pelo algoritimo de luhn
  if validarCartao(nmrCartao):
    bandeira = getBandeira(nmrCartao)
    print(bandeira)
  else:
    print("INVÁLIDO")
#algoritimo de luhn para definir a validade do cartao, e se valido, qual a bandeira do mesmo
def validarCartao(cartao):
  total = 0

  for i in range(len(cartao) - 2, -1, -2):
    vezesDois = int(cartao[i]) * 2
    if vezesDois > 9:
      total += vezesDois - 9
      #qualquer numero maior que 9 até 19 subtraido de 9, é o valor da soma dos proprios algarismos
    else:
      total += vezesDois

  for i in range(len(cartao) - 1, -1, -2):
    total += int(cartao[i])

  if total % 10 == 0:
    return True
  else
  return False
#após passar pela verificacao, aqui  é definido qual a bandeira do cartao seguindo as informacoes passadas no topico 2 do pset
def getBandeira(cartao):
  if (len(cartao) == 13 or len(cartao) == 16) and cartao[0] == '4':
    return 'VISA'

  if len(cartao) == 16 and cartao[0:2] in ['51', '52', '53', '54', '55']:
      return 'MASTERCARD'

  if len(cartao) == 15 and cartao[0:2] in ['34', '37']:
      return 'AMEX'

  return 'OUTRA BANDEIRA'

main()
