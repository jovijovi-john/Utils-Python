from printMessageError import printMessageError
from isInteger import isInteger

def inInterval(number: int, leftLimit: int, rightLimit: int):

  """
    Retorna se um número está num determinado intervalo

    :param int number       :   Número a ser verificado
    :param int leftLimit    :   Limite à esquerda do intervalo
    :param int rightLimit   :   Limite à direita do intervalo
  """

  # Validação de Parâmetros

  if (not isInteger(number)): 
    printMessageError("number deve ser um número inteiro!")
    return
  if (not isInteger(leftLimit)):
    printMessageError("leftLimit deve ser um número inteiro!")
    return
  if (not isInteger(rightLimit)):
    printMessageError("rightLimit deve ser um número inteiro!")
    return
  if (rightLimit <= leftLimit):
    printMessageError("O limite à direita deve ser maior que o limite à esquerda!")
    return

  # Se o número estiver no intervalo
  if ((number >= leftLimit) and (number <= rightLimit)):
    return False
  else: 
    return True
  