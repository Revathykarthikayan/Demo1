input_string = input("Enter a string: ")  # getting input
def most_freq(input_string):  # Defining a function
    max_char = None  # initilising to none
    max_count = 0  # initilising to 0

    for char in input_string:  # iteration for each char in string
        count = input_string.count(char)
        if count > max_count:  # checking for count value
            max_char = char  # max_char is updated
            max_count = count  # its count is taken as max_count

    if max_count == 1:  # If no character appears more than once
        return None
    else:
        return max_char  # returns the char with maximum count
result = most_freq(input_string)  #storeing the result of function most_freq
if result is None:
    print("No most frequent character")
else:
    print("Most frequent character:", result)
