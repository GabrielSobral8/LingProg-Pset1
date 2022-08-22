#algoritimo de luhn para definir a validade do cartao, e se valido, qual a bandeira do mesmo
def validarCartao(cartao):
  soma = 0

  for i in range(len(cartao) - 2, -1, -2):
    if int(cartao[i]) * 2 > 9:
      #qualquer numero maior que 9 até 19 subtraido de 9, é o valor da soma dos proprios algarismos
      soma += (int(cartao[i]) * 2) - 9
    else:
      soma += int(cartao[i]) * 2

  for i in range(len(cartao) - 1, -1, -2):
    soma += int(cartao[i])

  if soma % 10 == 0:
    return True
  else:
    return False

#após passar pela verificacao, aqui  é definido qual a bandeira do cartao seguindo as informacoes passadas no topico 2 do pset
def mostraBandeira(cartao):
  if cartao[0] == '4' and len(cartao) in [13, 16]:
        print('VISA')
  else:
      if cartao[0:2] in ['34', '37'] and len(cartao) == 15:
          print('AMEX')
      elif cartao[0:2] in ['51', '52', '53', '54', '55'] and len(cartao) == 16:
          print('MASTERCARD')
      else:
          print('INVÁLIDO')

nmrCartao = input("Insira o número do cartão de crédito: ")
#funcao para informar se é valido ou nao o numero do cartao após passar pelo algoritimo de luhn
if validarCartao(nmrCartao):
  mostraBandeira(nmrCartao)
else:
  print("INVÁLIDO")
