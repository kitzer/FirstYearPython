# JSON import
import json

book = {}

# Creating the record to store
book['tom'] = {
    'name': 'tom',
    'adress': '1 red street',
    'phone': 1234567
    }

# Creating second record
book['bob'] = {
    'name': 'bob',
    'address' : '1 green street',
    'phone' : 23412434
    }

# Dump the json to formatted string
s = json.dumps(book)
print(s)

# Creating the JSON file
f=open("book.json", "w")
f.write(s)
f.close()
