from colorama import Fore, Style

# Creating a class called Contact to assign the variables for each contact
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        
# Define the ContactBook class to manage the contact list.
class ContactBook:
    def __init__(self):
        self.contacts = [
            # Initialize the contact book with a list contacts
            Contact("alice", "1234567890", "alice@email.com"),
            Contact("bob", "9876543210", "bob@email.com")
        ]
        
    # Add a new contact to the contact book.
    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email)
        # Create a new Contact object with the provided details
        self.contacts.append(new_contact)
        print(Fore.GREEN + f"Contact '{name}' added successfully."+ Style.RESET_ALL)
        
    # Display all contacts in the contact book.
    def display_all_contacts(self):
        for contact in self.contacts:
            print(Fore.GREEN + f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}"+ Style.RESET_ALL)
    
    # Sort contacts alphabetically by name.(i did use chatGPT to help with this but i did research and understand lambda and the key parameter.)
    def sort_contacts(self):
        # Sort the contacts list by name.
        self.contacts.sort(key=lambda contact: contact.name.lower())
        print(Fore.GREEN + "Contacts have been sorted alphabetically."+ Style.RESET_ALL)

    # Search for a contact by name.
    def SearchContacts(self):
        #asking user for input
        find_contact = input("Type Name >").lower()
        for contact in self.contacts: #looping to find a contact
            if find_contact == contact.name:
                print (Fore.GREEN + f"Found Contacts: {contact.name}, {contact.phone_number}, {contact.email}"+ Style.RESET_ALL)
                return # exit the func once it has been matched
        print(Fore.RED + "No contact found with this name."+ Style.RESET_ALL)
            
    # Update an existing contact's details.
    def updateContacts(self):
        for contact in self.contacts:
            print(f"{contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        print (" Choose a name from your contacts to delete")
        user = input("choose Name > ").lower() #ask user to choose contact
        for contact in self.contacts: # loop through all contacts
            if user == contact.name:
                print (Fore.CYAN + f"Found Contacts: {contact.name}, {contact.phone_number}, {contact.email}") #printing contacts
                print(Fore.CYAN + "Is this the contact you want to change?\nA - Yes\nB - No"+ Style.RESET_ALL)
                user_delete = input("Choose > ").lower() #choose to delete contact or not.
            if user_delete == "yes": #if the user wants to update the contact
                self.contacts.remove(contact) #removes contact
                print(Fore.CYAN + "Please choose a new name number and email for your contact."+ Style.RESET_ALL)
                new_name = input("Choose Name > ").lower() #choosing new name
                new_phone_number = input("Choose Number > ").lower() #choosing new number
                new_email = input("Choose Email > ").lower() #choosing new email
                new_contact = Contact(new_name, new_phone_number, new_email) #create new contatc with updtaed details
                if new_phone_number or new_email in Contact: #this is to check duplicates
                    print (Fore.RED + "This contact already exsists. Please try again."+ Style.RESET_ALL)
                    new_name = input("Choose Name > ").lower() #if name exsists enter other details
                    new_phone_number = input("Choose Number > ").lower()
                    new_email = input("Choose Email > ").lower()
                else:
                    self.contacts.append(new_contact) #else if it isnt a dupe then append new details
                    print(Fore.GREEN + "Contact has been added.")
            elif user_delete == "no": #if user chooses no 
                print (Fore.CYAN + "Please choose a contact to delete."+ Style.RESET_ALL)
                user = input("choose Name > ") #asking to choose another contact
            else:
                print(Fore.RED + "Please type yes or no."+ Style.RESET_ALL) #if anything else is typed print this

    # Delete a contact by name.
    def DeleteContact(self):
        #display all contacts top choose wich one to delete.
        for contact in self.contacts:
            print(Fore.CYAN + f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}"+ Style.RESET_ALL)
        print(Fore.CYAN + "Which contact would you like to delete?"+ Style.RESET_ALL)
        delete_contact = input("Type Name >") #get the name of the contact you want to delete
        for contact in self.contacts:
            if delete_contact == contact.name:
                self.contacts.remove(contact) #remove contact from list
                print (Fore.GREEN + f"{contact.name} has been removed."+ Style.RESET_ALL) #confirming contact removed
    
# Main function to interact with ContactBook.
def main():
    contact_book = ContactBook()
    
    # Display the menu options to the user
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        print("2. Search For Contact")
        print("3. Display All Contacts")
        print("4. Delete Contacts")
        print("5. Update Contacts")
        print("6. Sort Contacts")
        print("0. Exit")

        choice = input("Enter your choice: ")
        #loop for actions in add contact func if 1 selected
        if choice == "1":
            name = input("Enter name: ").lower() #asking for new name, phone number and email.
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            if phone_number or email in Contact:
                print (Fore.RED + "This contact already exsists. Please try again."+ Style.RESET_ALL)#if contact already exsists try again
                name = input("Enter name: ").lower()
                phone_number = input("Enter phone number: ")
                email = input("Enter email: ")
            else:
                print(Fore.GREEN + "New contact has been created"+ Style.RESET_ALL) #if successful print this
                contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            contact_book.SearchContacts() #runs the search contact func if 2 selected
        elif choice == "3":
            contact_book.display_all_contacts() #displays all contacts func run if 3 selected
        elif choice == "4":
            contact_book.DeleteContact()# runs delete contact func if 4 is selected
        elif choice == "5":
            contact_book.updateContacts() #runs update contact fun if 5 is selected
        elif choice == "6":
            contact_book.sort_contacts() #this runs func that sorts the contacts.
        elif choice == "0":
            print(Fore.GREEN + "Exiting Contact Book. Goodbye!"+ Style.RESET_ALL) # if 0 selected then user exits the code
            break
        else:
            print(Fore.RED + "Please select an option with 1,2,3,4,5,0."+ Style.RESET_ALL) # if user enters anything other than 1,2,3,4,5,0 then this prints.

if __name__ == "__main__": # stops the program from auto running.
    main() # running main function.
