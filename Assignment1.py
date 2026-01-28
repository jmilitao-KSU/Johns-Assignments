# Assignment1.py
# Course: IT 3833 / Section 01
# Student Name : John Militao
# Assignment Number : Lab 1
# Due Date : 01/28/2026
# Purpose: This program implements a text-based menu, offering different options to manipulate an input buffer.

#Display menu options
print("Menu Options:")
print("1. Append data to input buffer")
print("2. Clear the input buffer")
print("3. Display current buffer")
print("4. Exit program")


#Implement first stage of input validation
while True:
    main_input = (input("Select what you would like to do: "))   
    try:
        main_input = int(main_input)
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")

#Main program loop, keeps iterating until user chooses to exit
input_buffer = ""
while main_input != 4:
    if main_input == 1:
        data_to_append = input("Enter data to append to the buffer: ")
        input_buffer += data_to_append
        print("Data appended successfully.")
    elif main_input == 2:
        input_buffer = ""
        print("Input buffer cleared.")
    elif main_input == 3:
        print("Current buffer content:", input_buffer)
    else:
        print("Invalid option. Please try again.")

    print("Menu Options:")
    print("1. Append data to input buffer")
    print("2. Clear the input buffer")
    print("3. Display current buffer")
    print("4. Exit program")

    while True:
        user_choice = input("Select what you would like to do: ")
        try:
            main_input = int(user_choice)
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


