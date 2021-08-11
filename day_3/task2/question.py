"""
Что выведет данный код? Почему?
"""
some_list = [[]] * 3
some_list[0].append(420)
print(some_list)

# [[420], [420], [420]]
# Элементы списка - есть ссылки на какой-либо объект. 
# При выполнениии [[]] * 3, мы создаем новые ссылки, а не объекты
# и т.к. append изменяет объект листа, а обхект у нас один, 
# то результат записался во все внутренние списки.




