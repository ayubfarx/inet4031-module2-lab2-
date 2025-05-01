
# INET4031 Module 1
#
# User List Processing Program
#
# Created: Nov 11, 2024
# Updated: Jan 6, 2025
#

def main():
    try:
        userFile = open("list-of-users.txt", "r")
    except Exception as e:
        print(f"\n[ERROR] Could not read the file: {e}")
        exit()

    # Load the lines of the file into a list
    listOfUsers = userFile.readlines()
    print("\nlist-of-users was read.")

    # Ask the user to proceed
    answer = input("\nDo you want to print out the list of users? (Y or N) ")

    if answer == "Y" or answer == "y":
        for userline in listOfUsers:
            print("\n", userline)
    else:
        print("\nOk not printing, ending...")

    print("\nEnd of User Processing\n")

# Run the main function
main()



