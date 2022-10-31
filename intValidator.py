def validateInt(msg="Digite um número: ", msgError="Digite um número válido"):
  try:
    number = input(msg)
    number = number.strip() # removendo os espaços em brancos
    number = int(number) # convertendo pra inteiro
  except ValueError:
    print(f"\033[1;31m{msgError}\033[m")
    validateInt(msg, msgError)