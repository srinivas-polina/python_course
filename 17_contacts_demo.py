#taking the dictionary of contact for our class and print out a list of only email addresses so that we can an email to the whole class.

contacts = {
    "number" : 4,
    "students" : [
        {"name" : "John Doe", "email" : "john.doe@example.com"},
        {"name" : "Bob Smith", "email" : "bob.smith@example.com"},
        {"name" : "Alice Johnson", "email" : "alice.johnson@example.com"},
        {"name" : "Charile Brown", "email" : "charlie.brown@example.com"}
    ]
}

print("Students Email Addresses: ")

for student in contacts["students"]:
    print(student["email"])
