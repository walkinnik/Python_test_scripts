# write the program that accepts 3 values - start time in hours + minutes format and duration time in minutes
# program should add duration time to the start time and give out the end time 
# if the end time will be on the next or in couple of days - it should also define that (so same day/in 1-x days)


def txt_writer(name, age, city):
    # function that accepts 3 values and stores them into the txt file
    test_file = open(r"./myfile.txt", "w+")
    test_file.write(f'Name: {name}\nAge: {age}\nCity: {city}')
    test_file.close()


def main():
    your_name = input("Enter your name: ")
    your_age = input("Enter your age: ")
    your_city = input("Enter your city: ")
    txt_writer(your_name,your_age,your_city)

    test_file = open("./myfile.txt", "r+")
    content_file = test_file.readlines()
    print(type(content_file))
    print(content_file[2])


if __name__ == '__main__':
    main()
