def unique_characters(input_string):
    # Useing set to store unique characters
    u_chars = set()
    # Iterate through the string and add each character to the set
    for char in input_string:
        u_chars.add(char) #appending char to set
    return list(u_chars)
input_string = input("Enter a string: ")
result = unique_characters(input_string)
print("Unique characters:", result)
