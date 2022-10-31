def isInteger(number):
  """
    Retorna uma entrada é um inteiro ou não

    :param str number:    Entrada que será verificada
  """
  number = number.strip() # removendo os espaços em brancos
  
  try:
    number = int(number)
    return True
  except ValueError:
    return False