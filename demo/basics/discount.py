# Take price and display discount @15%

# input
data = input("Enter price :")
price = int(data)  # Convert str to float

# process
discount = price * 15 // 100

# output
print('Discount =', discount)
