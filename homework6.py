a = int(input("Введите любое число"))
print("Hello my friend")
if a < 0:
    print("Ups, subzero")
print("BAY")
b = int(input("введите еще одно число"))
if a > b:
    print("a > b")
if a > b and a > 0:
    print("успех")
if a > b and (a > 0 or b < 1000):
    print("снова успех")
if 5 < b and b < 10:
    print("вновь успех")