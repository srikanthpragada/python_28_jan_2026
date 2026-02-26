from datetime import *

dates = []

for i in range(5):
    dob = input("Enter DOB [dd-mm-yyyy] :")
    dates.append(datetime.strptime(dob, "%d-%m-%Y"))

for d in sorted(dates):
    print(d.strftime("%d-%m-%Y"))
