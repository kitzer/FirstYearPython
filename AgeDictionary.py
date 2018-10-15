"""
Age dictionary
Matt Halliday
30/1/17
"""



#Dictionary
age = {"amy":17, "matt":17, "vicki":17, "oliver":14, "adam":19}

#Loop
while True:
    print(" ")
    print("===================")
    print(" ")

    #Default variables to addition
    counter=0
    adults=0

    #Asking user to input name and store
    search=input("Please enter the student name: ")
    #Printing the users eage
    print("This student is:", age.get(search.lower(), "Error: This student does not exsist."))

    #Mathematics for fidning the average
    for people in age:
        counter=counter+age[people]

    #Printing the average age
    print("Average age is",counter/len(age))

    #Selecting and finding users above the age of 18
    for people in age:
        if age[people] > int(18) :
            adults=adults+1
            print("There are", adults, "over 18.")




    print(" ")
    print("===================")
    print(" ")
