from utils.inInterval import inInterval
from utils.validateInt import validateInt

def intervalInputValidator(leftLimit, rightLimit, *msg, **kwargs):
  """
    Valida a entrada de um valor entre um determinado intervalo e retorna esse valor
    
    :param  float  leftLimit:    Limite da esquerda
    :param  float  rightLimit:   Limite da direita
    :param  str    msg :         Mensagem de erro
        exemplo: msg="informe um número entre @leftLimit e @rightLimit"
                  @leftLimit e @rightLimit serão substituidos por leftLimit e rightLimit respectivamente
    """
  
  input_number = validateInt(": ")
  # verifica se o número não está no intervalo
 
  if (not inInterval(input_number, leftLimit, rightLimit)):
    if (msg):
      msg = msg[0]

      if (not kwargs):
        msg = msg.replace("@leftLimit", str(leftLimit))
        msg = msg.replace("@rightLimit", str(rightLimit))

      print(f"\033[1;33m{msg}\033[m")
      return intervalInputValidator(leftLimit, rightLimit, msg, msgValidada=True)
    else:
      print(f"\033[1;33mInforme um número entre {leftLimit} e {rightLimit} \033[m")
      return intervalInputValidator(leftLimit, rightLimit)
  else:
    return input_number



# intervalInputValidator("10", "20", "informe um número entre @leftLimit e @rightLimit")

