contacts = {}
print("CONTACT BOOK")
print('<------------>')
print()
print('1.Add contact:')
print('2.Edit contact:')
print('3.View contact:')
print('4.Delete contact:')
print('5.Exit:')

while True:
    try:
        option = int(input('Enter option:'))
        
        if option == 1:
            name = input('Enter name:')
            number = int(input('Enter number:'))
            contacts[name] = number
            print(contacts)

        elif option == 2:
            print('1.Edit contact name:')
            print('2.Edit contact number:')
            try:
                opt = int(input('Enter option to edit:'))
                if opt == 1:
                    old_name = input('Enter old name:')
                    if old_name in contacts:
                        new_name = input('Enter new name:')
                        contacts[new_name] = contacts.pop(old_name)
                        print('Contact updated:', contacts)
                    else:
                        print('Contact not found')

                elif opt == 2:
                    old_name = input('Enter old name:')
                    if old_name in contacts:
                        new_no = int(input('Enter new number:'))
                        contacts[old_name] = new_no
                        print('Contact updated:', contacts)
                    else:
                        print("Contact not found")
                else:
                    print('Invalid option, please choose 1 or 2.')

            except ValueError:
                print('Invalid input, please enter a number for editing.')

        elif option == 3:
            print("Contacts:", contacts)

        elif option == 4:
            a = input('Enter name to delete:')
            if a in contacts:
                contacts.pop(a)
                print('Deleted:', a)
                print(contacts)
            else:
                print('Contact not found')

        elif option == 5:
            print('Exiting...')
            break

        else:
            print('Invalid option, please choose between 1 and 5.')

    except ValueError:
        print('Invalid input, please enter a number.')
