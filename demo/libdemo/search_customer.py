try:
    f = open("customers.txt", "rt")
    name = input("Enter customer name :")

    while True:
        line = f.readline()
        if line == "":  # EOF
            print('Sorry! Customer not found!')
            break

        if name.lower() in line.lower():
            print(f"Found customer with name : {line}")
            break

    f.close()
except Exception as ex:
    print('Error : ', ex)
