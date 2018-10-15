"""
Data Dictionary
Matt Halliday
30/01/17
"""
#Dictionary
stock = {"tables":12, "monitors":17, "chairs":17}

while True:

    search=input("Please enter the item: ")
    print(stock.get(search.lower(), "Error: Item not found." ))


    
"""
    # Storing the search
    stock_search = ""

    #Input stock
    while stock_search == "":
        stock_search=input("Please enter the word: ")
    #Printing stock m1
    for items in stock:
        if items == "tables":

    #Printing stock m2
    if stock_search in stock:
        print(stock[stock_search])
    else:
        print("Error: Sory this item is not in stock.")
"""
    
