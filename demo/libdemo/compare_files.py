# Compare two files and display where they differ, if differ

with  open('text1.txt', "rt") as f1, open("text2.txt", "rt") as f2:
    while True:
        line1 = f1.readline()
        line2 = f2.readline()

        if line1 == "" and line2 == "":
            print('Both files are same!')
            break

        if line1 != line2:
            if line1 == "":
                line1 = "EOF"
            if line2 == "":
                line2 = "EOF"

            print(f'Files differ at {line1} and {line2}')
            break



