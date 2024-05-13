string=input("ENTER THE STRING:")
def print_consonants(string):  #defining method
    vowels = 'aeiouAEIOU'
    char1=''
    for char in string:            # for loop for each character in string
        if char not in vowels:     # if condition checking for vowels
            char1 =char1+ char     #updateing char1 with new consonants
    return char1
if print_consonants(string):
    print(" New string after removing vowels:",print_consonants(string))
else:
    print('null')  # if no consonants avaiable in given string null is returned and  gets printed