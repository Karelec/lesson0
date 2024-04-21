immutable_var = [1,2,3,4],5,6,5.7,"кортеж", True
print(immutable_var)
print(type (immutable_var))
immutable_var[0][3] =2
print(immutable_var)
print("В квадратных скобках список, его можно изменить поэлементно, все остальное неизменяемо, однако, так же как и со строкой, кортеж можно вывести поэлементно.")
print("Например: ")
print(immutable_var[ 4: : -1])
print(type(immutable_var[5]))
mutable = [1,2,3,4,4.3,"список", True]
print("А это список ",mutable)
print(type(mutable[5]))
mutable[5] = 8
print(mutable)
print(type(mutable[5]))