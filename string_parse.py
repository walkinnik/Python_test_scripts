# Task:
# We have a long string with different words. Words can be repeated.
# Need calculate the number of words.
# HINT:  def should return dictionary {word: number}. Need read about split, lower, dict.get


def string_parse(string):
    # sets the string to lower case to avoid case-sensitiveness 
    string = string.lower()
    print(string)
    # set for keys - used to store unique keys (words) for dictionary from the string 
    keys_set = set()
    # dictionary with the results of the function
    result_dict = {}
    # splits the string and stores values
    string_separated = string.split()
    # adds first elemet to the result dict 
    #result_dict.update({str(string_separated[0]) : 1})
    # iterates throught the elements in separated string and adds unique keys to the keys_set
    for element in string_separated:
        keys_set.add(element)
    # iterates throught the elements in keys
    for key in keys_set:
        # iterates throught the elements in separated string and compares with key
        # counter used to count how many times unique key will meet word in separated string
        counter = 0
        for element in string_separated:
            # in case key meets the element from separated string it adds 1 to the counter
            if key == element:
                counter += 1
        # after each key iterates against the separated string key and it's counter is added to the result dict
        result_dict.update({key : counter})
    return result_dict 


def main():
    input_string = input("Write your string:")
    final_result = string_parse(input_string)
    print(final_result)
    print("Amount of unique words in the string: ", len(final_result))


if __name__ == '__main__':
    main()
