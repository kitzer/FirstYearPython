import csv
import os.path

file_exists = os.path.isfile('names3.csv')

first=input("Please enter your first name ")
last=input("Please enter your second name ")
age=int(input("Please enter your age "))

with open('names3.csv', 'a', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name','age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()
        writer.writerow({'first_name': first, 'last_name': last, 'age':str(age)})

    else:
        writer.writerow({'first_name': first, 'last_name': last, 'age':str(age)})
