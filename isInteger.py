def isInteger(number: str):
  """
    Retorna uma entrada é um inteiro ou não

    :param str number:    Entrada que será verificada
  """
  
  try:
    number = int(number)
    return True
  except ValueError:
    return False