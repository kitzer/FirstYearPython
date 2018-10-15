students={"John":17, "James":18, "Anna":17}

print(students["John"])

for names in students:
    print(names,students[names])

print(students.get("John"))
