from datetime import *
dates = []

i = 1
while i <= 5:
    try:
        dob = input("Enter DOB [dd-mm-yyyy] :")
        dates.append(datetime.strptime(dob, "%d-%m-%Y"))
        i += 1
    except ValueError:
        print("Sorry! Invalid Date. Please enter the correct format!")

for d in sorted(dates):
    print(d.strftime("%d-%m-%Y"))
