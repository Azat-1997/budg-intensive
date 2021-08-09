"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
# transmit_to_space("Test message") - выведет "Test message"
# т.к. message найдется в аргументах внешней функции.
# Далее будет напечатано "None": если функция ничего не возвращает (не имеет return <something>),
# то, по умоланию, возвращается None, который пропечатается внешним принтом

