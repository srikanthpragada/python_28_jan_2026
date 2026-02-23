
try:
    num = int(input("Enter number :"))
    print(100 / num)
except ValueError:
    print('Invalid input. Cannot be converted to int')
except ZeroDivisionError:
    print('Zero is not valid number!')
except Exception as ex:
    print('Error :', str(ex))

print('The End')


