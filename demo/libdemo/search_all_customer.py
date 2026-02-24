try:
    f = open("customers.txt", "rt")
    name = input("Enter customer name :")

    found = False
    while True:
        line = f.readline()
        if line == "":  # EOF
            break

        if name.lower() in line.lower():
            print(line, end  = '')
            found = True

    f.close()
    if not found:
        print('Sorry! No customer found!')
except Exception as ex:
    print('Error : ', ex)
