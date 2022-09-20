# better version of the first one, without while loop but with if elif else usage
# script asks for information and is able to save it in a file


def txt_writer(*args):
    # takes results of input_reader (3 values) and writes them in a txt file
    your_name = args[0][0]
    your_age = args[0][1]
    your_city = args[0][2]
    test_file = open(r"./myfile.txt", "w+")
    test_file.write(f'Name: {your_name}\nAge: {your_age}\nCity: {your_city}')
    test_file.close()


def input_reader():
    # asks for user's name, age and city
    your_name = input("Enter your name: ")
    your_age = input("Enter your age: ")
    your_city = input("Enter your city: ")
    return your_name, your_age, your_city


def main():
    # greets user, asks if a user wants to start / save entered information aborts in case of entering unsupported value
    # anything else than Y or N
    greeting_message = input("Hello! Would you like to start? (Y/N): ")
    if greeting_message == "Y" or greeting_message == "N":
        if greeting_message == "Y":
            returned_values = input_reader()
            write_message = input("Would you like to write your information in base? (Y/N): ")
            if write_message == "Y" or write_message == "N":
                if write_message == "Y":
                    txt_writer(returned_values)
                    print("Values added, have a nice day!")
                elif write_message == "N":
                    print("Values not added, have a nice day!")
            else:
                print("Entered value is not valid, please try again")
        elif greeting_message == "N":
            print("Goodbye!")
    else:
        print("Entered value is not valid, please try again")


if __name__ == '__main__':
    main()