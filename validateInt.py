from utils.isInteger import isInteger
from utils.printMessageError import printMessageError

def validateInt(msg="Digite um número: ", msgError="Digite um número válido"):
  """
    Faz um loop que só para quando o usuário informar um inteiro válido

    :param str msg:       Mensagem mostrada no input
    :param str msgError:  Mensagem mostrada quando o usuário informa um número inválido
  """
  number = input(msg)    
  
  if (isInteger(number)):
    return int(number)
  else:
    printMessageError(msgError)
    return validateInt(msg, msgError)

