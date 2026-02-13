def mathoperation(n1, n2, task):
    print(task(n1, n2))

def add(n1, n2):
    return n1 + n2

def square(n):
    return n * n

mathoperation(10, 20, add)
#mathoperation(10, 20, square)
