import os
import string
import random

while True:
    user_choice = int(input("Enter 1 to generate files in your chosen folder, 2 to generate files in a folder called 'Generated Files', or 3 to end the program: "))

    if user_choice == 1:
        folder_name = input("Enter the name of the folder where you want to generate files: ")
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")

        while True:
            file_name_choice = input("Enter 1 to generate random file names, 2 to input file names one by one, or 3 to go back to main menu: ")

            if file_name_choice == "1":
                # generate 35 .json files with random names
                for i in range(35):
                    file_name = ''.join(random.choices(string.ascii_lowercase, k=10)) + ".json"
                    with open(os.path.join(folder_name, file_name), "w") as f:
                        pass  # no content to write

                # print out the file names in alphabetical order
                file_names = sorted(os.listdir(folder_name))
                for file_name in file_names:
                    print(file_name)

            elif file_name_choice == "2":
                # input file names one by one
                while True:
                    file_name = input("Enter file name or type 'exit' to go back to previous menu: ")
                    if file_name == "exit":
                        break
                    with open(os.path.join(folder_name, file_name), "w") as f:
                        pass  # no content to write

                # print out the file names in alphabetical order
                file_names = sorted(os.listdir(folder_name))
                for file_name in file_names:
                    print(file_name)

            elif file_name_choice == "3":
                break  # go back to main menu
            else:
                print("Invalid choice. Try again.")
                continue

    elif user_choice == 2:
        folder_name = "Generated Files"
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")

        # prompt user for number of files and character count
        num_files = int(input("Enter the number of files to generate: "))
        char_count = int(input("Enter the number of characters in each file name: "))

        # generate .json files with random names
        for i in range(num_files):
            file_name = ''.join(random.choices(string.ascii_lowercase, k=char_count)) + ".json"
            with open(os.path.join(folder_name, file_name), "w") as f:
                pass  # no content to write

        # print out the file names in alphabetical order
        file_names = sorted(os.listdir(folder_name))
        for file_name in file_names:
            print(file_name)

    elif user_choice == 3:
        print("Exiting program.")
        break

    else:
        print("Invalid")
