def printMessageError(msg: str):
  """
    Printa uma mensagem em vermelho

    :param str msg: Mensagem a ser printada
  """

  #futuramente, implementar a cor dinamicamente
  print(f"\033[1;31m{msg}\033[m")