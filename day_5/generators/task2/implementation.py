def return_errors(filename):
    """
    Функция, которая возвращает строки из лога со словом error
    """
    with open(filename) as file:
       for line in file:
          if "error" in line.lower():
             yield line


return_errors('log.txt')
