my_string = input("Ваш жизненный девиз: ")
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ", "#"))
print(my_string[0])
print(my_string[-1])
print("Сможете быстро повторить?: ",my_string[ : :-1])
input("Шучу, как Ваше имя? ")
year = int(input("Напомните, какой сейчас год? "))
print(type(year))
birth = int(input("В каком году Вы родились? "))
print(type(birth))
year_now = year - birth
print("по моим подчетам Вам ", year_now, "лет")
