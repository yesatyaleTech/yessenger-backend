import pymongo
from pymongo import MongoClient
from bson import ObjectId

client = pymongo.MongoClient('localhost:27017')

db = client['testDB']
collection = db.testCollection

# Create a contact

def create_contact():
    first_name = str(input("First Name: "))
    last_name = str(input("Last Name: "))
    phone_number = str(input("Phone Number: "))
    email = str(input("Email Address: "))
    team = str(input("Team/Company: "))

    record = {
        "first_name":first_name,
        "last_name":last_name,
        "name": first_name+" "+last_name,
        "phone_number": phone_number,
        "email": email,
        "team": team
        }
        
    return record

#-----------------------------------------------------------------------------------------------------------------------------------------

# Get and Set functions
def get_contact_id(contact):
    return str(contact["_id"])

def get_first_name(contact):
    return contact["first_name"]

def get_last_name(contact):
    return contact["last_name"]

def get_name(contact):
    return contact["name"]

def get_phone_number(contact):
    return contact["phone_number"]

def get_email(contact):
    return contact["email"]

def get_team(contact):
    return contact["team"]

def set_contact_id(new_id, contact):
    contact["_id"] = new_id
    return contact

def set_name(contact):
    contact["name"] = contact["first_name"] + " " + contact["last_name"]
    return contact

def set_first_name(new_first_name, contact):
    contact["first_name"] = new_first_name
    set_name(contact)
    return contact

def set_last_name(new_last_name, contact):
    contact["last_name"] = new_last_name
    set_name(contact)
    return contact

def set_phone_number(new_phone_number, contact):
    contact["phone_number"] = new_phone_number
    return contact

def set_email(new_email, contact):
    contact["email"] = new_email
    return contact

def set_team(new_team, contact):
    contact["team"] = new_team
    return contact

#----------------------------------------------------------------------------------------------------------------------------------------
def printer(i):
    first_name = get_first_name(i)
    last_name = get_last_name(i)
    name = get_name(i)
    phone_number = get_phone_number(i)
    email = get_email(i)
    team = get_team(i)
    print(          "ID: ", get_contact_id(i),
        "\nName: ", name,
                    "\nPhone number: ", phone_number, "\nEmail Address: ", email,
                    "\nTeam: ", team)

#---------------------------------------------------------------------------------------------------------------------------------------

def check_id(id):
    status = True
    for contact in collection.find():
        if get_contact_id(contact) == id:
            status = False
            break
        
    return status

#---------------------------------------------------------------------------------------------------------------------------------------
def menu():
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search a contact")
    print("5. Display all contacts")
    print("6. Edit contacts")
    print("Any other key - To exit")
    choice = int(input("Please enter your choice: "))

    return choice

def add(contact): #DONE
    return collection.insert_one(contact)

def remove(query): #DONE
    
    temp = 0

    for i in collection.find():
        if get_first_name(i) == query:
            temp += 1
            collection.delete_one(i)
        elif get_last_name(i) == query:
            temp+= 1
            collection.delete_one(i)

    if temp == 0:
        print("Sorry, you have entered an invalid query.\
Please recheck and try again later.")

def delete_all(): #DONE
    return collection.delete_many({})

def search_existing(query): #DONE
    check = -1
    for contact in collection.find():
        if query == get_first_name(contact):
            check = contact
            printer(contact)
        elif query == get_last_name(contact):
            check = contact
            printer(contact)

    if check == -1:
        return -1
    else:
        return check

def display_all():
    if collection.count == 0:
        print("List is empty: []")
    else:
        for contact in collection.find():
            printer(contact)
            print("------------------------------------------------------------------")

def edit_contact(i, contact):
    temp = search_existing(contact)
    printer(contact)
    
    if i == "1": # Edit First Name
        current_first_name = get_first_name(contact)
        print("Current First Name: ", current_first_name)
        new_first_name = str(input("New First Name: "))
        new_id = ObjectId()
        updated_contact = set_first_name(new_first_name, contact)
        collection.delete_one(contact)
        collection.delete_many(contact)

        while True:
            if(check_id(new_id)):
                updated_contact = set_contact_id(new_id, updated_contact)
                break
            else:
                new_id = ObjectId()
        
        add(updated_contact)
        
        print("Edit Complete!")
        print("**************************************************************")
        printer(contact)
        print("##############################################################")
        printer(updated_contact)
        print("**************************************************************")
        
        return updated_contact

    elif i == "2": # Edit Last Name
        current_last_name = get_last_name(contact)
        print("Current Last Name: ", current_last_name)
        new_last_name = str(input("New Last Name: "))
        contact = set_last_name(new_last_name, contact)
        print("Edit Complete!")
        printer(contact)
        return contact

    elif i == "3": # Edit Phone Number
        current_phone_number = get_phone_number(contact)
        print("Current Phone Number: ", current_phone_number)
        new_phone_number = str(input("New Phone Number: "))
        contact = set_phone_number(new_phone_number, contact)
        print("Edit Complete!")
        printer(contact)
        return contact

    elif i == "4": # Edit Email Address
        current_email = get_email(contact)
        print("Current Email Address: ", current_email)
        new_email = str(input("New Email Address: "))
        contact = set_email(new_email, contact)
        print("Edit Complete!")
        printer(contact)
        return contact
        
    elif i == "5": # Edit Team/Company
        current_team = get_team(contact)
        print("Current Team/Company: ", current_team)
        new_team = str(input("New Team/Company: "))
        contact = set_team(new_team, contact)
        print("Edit Complete!")
        printer(contact)
        return contact
    
    else:
        print("Invalid Editing Option")


#def sort_contacts():

#def create_group(): #group will be an array of contact fields

#def add_to_group(): #add a contact field to the array of contact fields

#def remove_from_group(): #remove a contact from an array of contact fields

#def 

#-----------------------------------------------------------------------------------------------------------------------
                
option = 1

while True:

    option = menu()
    if option == 1:
        add(create_contact())

    elif option == 2:
        query = str(input("Name: "))
        remove(query)

    elif option == 3:
        delete_all()

    elif option == 4:
        query = str(input("Name: "))
        d = search_existing(query)
        if d == -1:
            print("The contact does not exist")

    elif option == 5:
        display_all()
    
    elif option == 6:
        query = str(input("Name: "))
        printer(search_existing(query))
        print(" 1 - Edit First Name\n 2 - Edit Last Name\n 3 - Edit Phone Number\n 4 - Edit Email Address\n 5 - Edit Team/Company")
        i = str(input("Option: "))
        edit_contact(i, search_existing(query))
    else:
        break


