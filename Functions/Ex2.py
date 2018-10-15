# Function
def calculateArea(x,y):
    result=x*y
    return result

# Main program
width=int(input("Please enter your width "))
height=int(input("Please enter your height "))
#Call the function and passing 2 values(arguments) into it

# Go and find the area by calling the function
area = calculateArea(height,width)
# Printing the area
print("Area =" , area)

