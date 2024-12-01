# Take user input
length = input("Please type length (in meters): \n")
width = input("Please type width (in meters): \n")
price = input("How much for one meter? : \n")

# Convert input strings to floats
f_length = float(length)
f_width = float(width)
f_price = float(price)

# Calculate area and total price
area = f_length * f_width
total_price = f_price * area

# Display results
print("The total area is: {:.2f} square meters".format(area))
print("Give the guy: ${:.2f}".format(total_price))
