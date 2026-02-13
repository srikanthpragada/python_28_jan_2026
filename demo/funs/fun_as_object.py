def fun():
    print('A function')

a = 10
b = a

f = fun
f()
fun()
print(a, b)
print(id(a), id(fun))