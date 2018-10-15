# Function
def calculateParimeter(x,y):
    result=x+y+x+y
    return result

# Main program
height=int(input("Please enter your 1st side "))
width=int(input("Please enter your 2nd side "))
#Call the function and passing 2 values(arguments) into it

# Go and find the area by calling the function
parimeter = calculateParimeter(height,width)
# Printing the parimeter
print("parimeter =" , parimeter)

